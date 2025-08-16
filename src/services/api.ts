const API_BASE_URL = 'http://localhost:8000';

export interface Assignment {
  assignment_id: string;
  title: string;
  status: 'draft' | 'published';
  canvas_json: unknown[];
}

export const createNewAssignment = async (title: string): Promise<Assignment> => {
  const response = await fetch(`${API_BASE_URL}/api/assignments/`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ title }),
  });

  if (!response.ok) {
    throw new Error('Failed to create assignment');
  }

  return response.json();
};
