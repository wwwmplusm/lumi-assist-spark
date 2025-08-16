import { X, User } from 'lucide-react';
import { useAppStore, MenuItem } from '../stores/appStore';
import { Button } from './ui/button';
import {
  HoverCard,
  HoverCardContent,
  HoverCardTrigger,
} from '@/components/ui/hover-card';

// Sub-component for a single menu item to keep the main component clean
const SidebarMenuItem = ({ item }: { item: MenuItem }) => {
  const Icon = item.icon;

  const menuItemContent = (
    <Button
      variant="ghost"
      className="w-full justify-start p-4 h-auto text-base text-gray-700 hover:bg-gray-800 hover:text-white"
    >
      <Icon size={20} className="mr-3" />
      <span className="font-medium">{item.label}</span>
    </Button>
  );

  if (!item.subMenu) {
    return <div>{menuItemContent}</div>;
  }

  return (
    <HoverCard openDelay={100} closeDelay={100}>
      <HoverCardTrigger asChild>
        <div>{menuItemContent}</div>
      </HoverCardTrigger>
      <HoverCardContent
        side="right"
        align="start"
        className="ml-2 w-72 p-4"
      >
        <h3 className="font-semibold mb-3 text-gray-800">{item.subMenu.title}</h3>
        <div className="space-y-2">
          {item.subMenu.items.map((subItem) => (
            <div
              key={subItem.label}
              className="p-2 hover:bg-gray-100 rounded-lg cursor-pointer"
            >
              <div className="font-medium text-gray-800">{subItem.label}</div>
              {subItem.details && (
                <div className="text-sm text-gray-600">{subItem.details}</div>
              )}
            </div>
          ))}
        </div>
      </HoverCardContent>
    </HoverCard>
  );
};

const Sidebar = () => {
  const { isSidebarOpen, toggleSidebar, menuItems } = useAppStore();

  return (
    <>
      {isSidebarOpen && (
        <div
          className="fixed inset-0 bg-black bg-opacity-50 z-40"
          onClick={toggleSidebar}
        />
      )}
      <div
        className={`
          fixed top-0 left-0 h-full w-80 bg-white z-50 transform transition-transform duration-300 ease-in-out
          ${isSidebarOpen ? 'translate-x-0' : '-translate-x-full'}
        `}
      >
        <div className="flex items-center justify-between p-6 border-b border-gray-300">
          <h2 className="text-xl font-semibold text-gray-800">Меню</h2>
          <Button
            variant="ghost"
            size="icon"
            onClick={toggleSidebar}
            className="h-auto p-2"
          >
            <X size={20} className="text-gray-600" />
          </Button>
        </div>
        <div className="p-4 space-y-2">
          {menuItems.map((item) => (
            <SidebarMenuItem key={item.id} item={item} />
          ))}
        </div>
      </div>
    </>
  );
};

export default Sidebar;

