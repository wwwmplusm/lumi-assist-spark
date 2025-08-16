import { useAppStore } from '../stores/appStore';

const HamburgerMenu = () => {
  const { isSidebarOpen, toggleSidebar } = useAppStore();
  return (
    <button
      onClick={toggleSidebar}
      className="fixed top-6 left-6 z-50 w-12 h-12 flex flex-col justify-center items-center space-y-1.5 hover:bg-white/10 rounded-lg transition-colors"
    >
      <div className={`hamburger-line w-6 h-0.5 ${isSidebarOpen ? 'rotate-45 translate-y-2' : ''}`} />
      <div className={`hamburger-line w-6 h-0.5 ${isSidebarOpen ? 'opacity-0' : ''}`} />
      <div className={`hamburger-line w-6 h-0.5 ${isSidebarOpen ? '-rotate-45 -translate-y-2' : ''}`} />
    </button>
  );
};

export default HamburgerMenu;
