import { z } from 'zod';
import { useAuthStore } from '@/store/authStore';

const API_BASE_URL = 'http://localhost:8000';

export class ApiError extends Error {
  constructor(public status: number, message: string) {
    super(message);
    this.name = 'ApiError';
  }
}

export async function api<T>(
  path: string,
  schema: z.ZodSchema<T>,
  options?: RequestInit
): Promise<T> {
  const teacherId = useAuthStore.getState().teacherId;
  const headers = new Headers(options?.headers);
  if (!headers.has('Content-Type')) {
    headers.set('Content-Type', 'application/json');
  }
  if (teacherId) {
    headers.set('X-Teacher-ID', teacherId);
  }

  const response = await fetch(`${API_BASE_URL}${path}`, { ...options, headers });

  if (!response.ok) {
    const errorText = await response.text();
    throw new ApiError(response.status, errorText || 'API request failed');
  }
  
  if (response.headers.get("Content-Length") === "0" || response.status === 204) {
    return schema.parse(null);
  }

  const data = await response.json();
  const result = schema.safeParse(data);

  if (!result.success) {
    console.error("Zod validation error:", result.error.flatten());
    throw new Error('Invalid data structure received from server.');
  }
  return result.data;
}
