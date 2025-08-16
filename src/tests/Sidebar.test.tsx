import { render, screen } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import { describe, it, expect } from 'vitest';
import Sidebar from '@/components/Sidebar';
import { useAppStore } from '@/stores/appStore';
import { act } from 'react';

describe('Sidebar Component', () => {
  it('should render all menu items from the store', () => {
    render(<Sidebar />);

    expect(screen.getByText('Личный кабинет')).toBeInTheDocument();
    expect(screen.getByText('Ученики')).toBeInTheDocument();
    expect(screen.getByText('Ассистент Lumi')).toBeInTheDocument();
    expect(screen.getByText('Библиотека')).toBeInTheDocument();
  });

  it('should show a hover card with student list when hovering over "Ученики"', async () => {
    const user = userEvent.setup();
    render(<Sidebar />);
    const studentsMenuItem = screen.getByText('Ученики');

    await user.hover(studentsMenuItem);

    expect(await screen.findByText('Список учеников')).toBeVisible();
    expect(screen.getByText('Гриша Иванов')).toBeVisible();
  });

  it('should be hidden by default and appear when store state changes', () => {
    const { container } = render(<Sidebar />);

    const sidebarContainer = container.querySelector('.transform');
    expect(sidebarContainer).toHaveClass('-translate-x-full');

    act(() => {
      useAppStore.getState().toggleSidebar();
    });

    expect(sidebarContainer).toHaveClass('translate-x-0');
  });
});
