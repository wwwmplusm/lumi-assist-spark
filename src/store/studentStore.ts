import { create } from 'zustand';
import { getStudents, type Student } from '@/api/teacherApi';

type StudentState = {
  students: Student[];
  fetchStudents: () => Promise<void>;
};

export const useStudentStore = create<StudentState>((set) => ({
  students: [],
  fetchStudents: async () => {
    try {
      const students = await getStudents();
      set({ students });
    } catch (error) {
      console.error("Failed to fetch students", error);
    }
  },
}));
