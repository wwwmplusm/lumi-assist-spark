import { create } from 'zustand';
import { persist } from 'zustand/middleware';

type AuthState = {
  teacherId: string | null;
  setTeacherId: (id: string) => void;
};

export const useAuthStore = create<AuthState>()(
  persist(
    (set) => ({
      teacherId: null, // Изначально ID нет
      setTeacherId: (id) => set({ teacherId: id }),
    }),
    { name: 'auth-storage' } // Сохраняем ID в localStorage
  )
);
