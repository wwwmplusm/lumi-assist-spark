import { useState } from 'react';
import HamburgerMenu from '../components/HamburgerMenu';
import Sidebar from '../components/Sidebar';
import PromptInput from '../components/PromptInput';

const Index = () => {
  const [isSidebarOpen, setIsSidebarOpen] = useState(false);

  return (
    <div className="min-h-screen tech-grid-bg relative overflow-hidden">
      {/* Hamburger Menu */}
      <HamburgerMenu 
        isOpen={isSidebarOpen}
        onClick={() => setIsSidebarOpen(!isSidebarOpen)}
      />

      {/* Sidebar */}
      <Sidebar 
        isOpen={isSidebarOpen}
        onClose={() => setIsSidebarOpen(false)}
      />

      {/* Main Content */}
      <div className="min-h-screen flex items-center justify-center px-4">
        <div className="text-center max-w-4xl">
          <h1 className="text-5xl md:text-6xl lg:text-7xl font-bold neon-glow mb-8 leading-tight">
            Lumi AI — ваш главный помощник в сфере образования
          </h1>
        </div>
      </div>

      {/* Prompt Input */}
      <PromptInput />
    </div>
  );
};

export default Index;
