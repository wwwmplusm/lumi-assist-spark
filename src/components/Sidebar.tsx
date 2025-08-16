import { useState } from 'react';
import { X, User, Users, Bot, Library, FolderOpen, FileText } from 'lucide-react';

interface SidebarProps {
  isOpen: boolean;
  onClose: () => void;
}

const Sidebar = ({ isOpen, onClose }: SidebarProps) => {
  const [hoveredItem, setHoveredItem] = useState<string | null>(null);
  const [expandedSubMenu, setExpandedSubMenu] = useState<string | null>(null);

  const handleItemHover = (item: string) => {
    setHoveredItem(item);
    setExpandedSubMenu(item);
  };

  const handleItemLeave = () => {
    setHoveredItem(null);
    // Keep submenu open briefly for better UX
    setTimeout(() => setExpandedSubMenu(null), 200);
  };

  return (
    <>
      {/* Overlay */}
      {isOpen && (
        <div 
          className="fixed inset-0 bg-black bg-opacity-50 z-40"
          onClick={onClose}
        />
      )}

      {/* Sidebar */}
      <div className={`
        fixed top-0 left-0 h-full w-80 bg-white z-50 transform transition-transform duration-300 ease-in-out
        ${isOpen ? 'translate-x-0' : '-translate-x-full'}
      `}>
        {/* Header */}
        <div className="flex items-center justify-between p-6 border-b border-gray-300">
          <h2 className="text-xl font-semibold text-gray-800">Меню</h2>
          <button 
            onClick={onClose}
            className="p-2 hover:bg-gray-200 rounded-lg transition-colors"
          >
            <X size={20} className="text-gray-600" />
          </button>
        </div>

        {/* Menu Items */}
        <div className="p-4 space-y-2">
          {/* Личный кабинет */}
          <div 
            className="relative"
            onMouseEnter={() => handleItemHover('profile')}
            onMouseLeave={handleItemLeave}
          >
            <div className="p-4 rounded-lg cursor-pointer flex items-center space-x-3 text-gray-700 hover:bg-gray-800 hover:text-white transition-colors">
              <User size={20} />
              <span className="font-medium">Личный кабинет</span>
            </div>
            
            {expandedSubMenu === 'profile' && (
              <div className="absolute left-full top-0 ml-2 w-64 bg-white rounded-lg p-4 shadow-xl border border-gray-200 z-50">
                <div className="flex items-center space-x-3">
                  <div className="w-12 h-12 bg-gray-300 rounded-full flex items-center justify-center">
                    <User size={24} className="text-gray-600" />
                  </div>
                  <div>
                    <h3 className="font-semibold text-gray-800">Светлана</h3>
                    <p className="text-sm text-gray-600">учитель русского языка</p>
                  </div>
                </div>
              </div>
            )}
          </div>

          {/* Ученики */}
          <div 
            className="relative"
            onMouseEnter={() => handleItemHover('students')}
            onMouseLeave={handleItemLeave}
          >
            <div className="p-4 rounded-lg cursor-pointer flex items-center space-x-3 text-gray-700 hover:bg-gray-800 hover:text-white transition-colors">
              <Users size={20} />
              <span className="font-medium">Ученики</span>
            </div>
            
            {expandedSubMenu === 'students' && (
              <div className="absolute left-full top-0 ml-2 w-72 bg-white rounded-lg p-4 shadow-xl border border-gray-200 z-50">
                <h3 className="font-semibold mb-3 text-gray-800">Список учеников</h3>
                <div className="space-y-2">
                  <div className="p-2 hover:bg-gray-100 rounded-lg cursor-pointer">
                    <div className="font-medium text-gray-800">Гриша Иванов</div>
                    <div className="text-sm text-gray-600">11 класс</div>
                  </div>
                  <div className="p-2 hover:bg-gray-100 rounded-lg cursor-pointer">
                    <div className="font-medium text-gray-800">Соня Сергеева</div>
                    <div className="text-sm text-gray-600">9 класс</div>
                  </div>
                  <div className="p-2 hover:bg-gray-100 rounded-lg cursor-pointer">
                    <div className="font-medium text-gray-800">Маша Журавлева</div>
                    <div className="text-sm text-gray-600">10 класс</div>
                  </div>
                </div>
              </div>
            )}
          </div>

          {/* Ассистент Lumi */}
          <div className="p-4 rounded-lg cursor-pointer flex items-center space-x-3 text-gray-700 hover:bg-gray-800 hover:text-white transition-colors">
            <Bot size={20} />
            <span className="font-medium">Ассистент Lumi</span>
          </div>

          {/* Библиотека */}
          <div 
            className="relative"
            onMouseEnter={() => handleItemHover('library')}
            onMouseLeave={handleItemLeave}
          >
            <div className="p-4 rounded-lg cursor-pointer flex items-center space-x-3 text-gray-700 hover:bg-gray-800 hover:text-white transition-colors">
              <Library size={20} />
              <span className="font-medium">Библиотека</span>
            </div>
            
            {expandedSubMenu === 'library' && (
              <div className="absolute left-full top-0 ml-2 w-56 bg-white rounded-lg p-4 shadow-xl border border-gray-200 z-50">
                <div className="space-y-2">
                  <div className="p-3 hover:bg-gray-100 rounded-lg cursor-pointer flex items-center space-x-3 text-gray-700">
                    <FolderOpen size={18} />
                    <span>Материалы</span>
                  </div>
                  <div className="p-3 hover:bg-gray-100 rounded-lg cursor-pointer flex items-center space-x-3 text-gray-700">
                    <FileText size={18} />
                    <span>Домашнее задание</span>
                  </div>
                </div>
              </div>
            )}
          </div>
        </div>
      </div>
    </>
  );
};

export default Sidebar;
