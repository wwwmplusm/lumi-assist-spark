import { create } from 'zustand';
import { User, Users, Bot, Library, LucideIcon } from 'lucide-react';

// Define types for our menu structure
export interface SubMenuItem {
  label: string;
  details?: string;
}

export interface MenuItem {
  id: string;
  label: string;
  icon: LucideIcon;
  subMenu?: {
    title: string;
    items: SubMenuItem[];
  };
}

interface AppState {
  isSidebarOpen: boolean;
  toggleSidebar: () => void;
  menuItems: MenuItem[];
}

// Define the menu data
const initialMenuItems: MenuItem[] = [
  { id: 'profile', label: 'Личный кабинет', icon: User },
  {
    id: 'students',
    label: 'Ученики',
    icon: Users,
    subMenu: {
      title: 'Список учеников',
      items: [
        { label: 'Гриша Иванов', details: '11 класс' },
        { label: 'Соня Сергеева', details: '9 класс' },
        { label: 'Маша Журавлева', details: '10 класс' },
      ],
    },
  },
  { id: 'assistant', label: 'Ассистент Lumi', icon: Bot },
  { id: 'library', label: 'Библиотека', icon: Library },
];

export const useAppStore = create<AppState>((set) => ({
  isSidebarOpen: false,
  toggleSidebar: () => set((state) => ({ isSidebarOpen: !state.isSidebarOpen })),
  menuItems: initialMenuItems,
}));

