import { z } from 'zod';
import { api } from './client';

export const StudentSchema = z.object({
  id: z.string(),
  name: z.string(),
  email: z.string().email().nullable(),
});
export type Student = z.infer<typeof StudentSchema>;

export const StudentsResponseSchema = z.array(StudentSchema);

// API-функция для получения списка студентов
export const getStudents = () => api('/api/teacher/students', StudentsResponseSchema);
