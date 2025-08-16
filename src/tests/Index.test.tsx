import { render, screen } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import { describe, it, expect, vi, afterEach } from 'vitest';
import Index from '@/pages/Index';
import * as api from '@/services/api';

vi.mock('@/services/api', () => ({
  createNewAssignment: vi.fn(),
}));

afterEach(() => {
  vi.clearAllMocks();
});

describe('Index Page', () => {
  it('should render the main heading and the test button', () => {
    render(<Index />);

    expect(screen.getByRole('heading', { name: /Lumi AI/i })).toBeInTheDocument();
    expect(
      screen.getByRole('button', { name: /Test Create Assignment API/i })
    ).toBeInTheDocument();
  });

  it('should call the createNewAssignment API when the test button is clicked', async () => {
    const user = userEvent.setup();
    const mockAssignment = {
      assignment_id: 'test-uuid-123',
      title: 'My Test Assignment',
      status: 'draft',
      canvas_json: [],
    };
    vi.mocked(api.createNewAssignment).mockResolvedValue(mockAssignment);
    const alertMock = vi.spyOn(window, 'alert').mockImplementation(() => {});

    render(<Index />);
    const testButton = screen.getByRole('button', { name: /Test Create Assignment API/i });

    await user.click(testButton);

    expect(api.createNewAssignment).toHaveBeenCalledOnce();
    expect(api.createNewAssignment).toHaveBeenCalledWith('My Test Assignment');
    expect(alertMock).toHaveBeenCalledWith('Assignment created with ID: test-uuid-123');

    alertMock.mockRestore();
  });

  it('should show an alert if the API call fails', async () => {
    const user = userEvent.setup();
    vi.mocked(api.createNewAssignment).mockRejectedValue(new Error('API is down'));
    const alertMock = vi.spyOn(window, 'alert').mockImplementation(() => {});

    render(<Index />);
    const testButton = screen.getByRole('button', { name: /Test Create Assignment API/i });

    await user.click(testButton);

    expect(api.createNewAssignment).toHaveBeenCalledOnce();
    expect(alertMock).toHaveBeenCalledWith('Failed to create assignment. Check the console.');

    alertMock.mockRestore();
  });
});
