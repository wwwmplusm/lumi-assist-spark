import { useState } from 'react';
import { Plus, Upload, CloudDownload } from 'lucide-react';

const PromptInput = () => {
  const [isDropdownOpen, setIsDropdownOpen] = useState(false);

  return (
    <div className="fixed bottom-6 left-1/2 transform -translate-x-1/2 w-full max-w-2xl px-4">
      <div className="relative">
        <input
          type="text"
          placeholder="Что вы хотите создать сегодня?"
          className="prompt-input w-full px-6 py-4 pr-16 rounded-full border text-lg focus:outline-none focus:ring-2 focus:ring-blue-400 transition-all"
        />
        
        {/* Plus Button with Dropdown */}
        <div className="absolute right-3 top-1/2 transform -translate-y-1/2">
          <button
            onClick={() => setIsDropdownOpen(!isDropdownOpen)}
            className="w-10 h-10 bg-black rounded-full flex items-center justify-center hover:bg-gray-800 transition-colors"
          >
            <Plus size={20} className="text-white" />
          </button>
          
          {/* Dropdown Menu */}
          {isDropdownOpen && (
            <>
              {/* Backdrop */}
              <div 
                className="fixed inset-0 z-10"
                onClick={() => setIsDropdownOpen(false)}
              />
              
              {/* Dropdown Content */}
              <div className="absolute bottom-full right-0 mb-2 w-64 bg-white rounded-lg shadow-xl border border-gray-200 z-30 p-2">
                <button 
                  className="w-full text-left p-3 hover:bg-gray-100 rounded-lg flex items-center space-x-3 text-gray-700 transition-colors"
                  onClick={() => setIsDropdownOpen(false)}
                >
                  <Upload size={18} />
                  <span>добавить файлы и фотографии</span>
                </button>
                <button 
                  className="w-full text-left p-3 hover:bg-gray-100 rounded-lg flex items-center space-x-3 text-gray-700 transition-colors"
                  onClick={() => setIsDropdownOpen(false)}
                >
                  <CloudDownload size={18} />
                  <span>добавить из Google Drive</span>
                </button>
              </div>
            </>
          )}
        </div>
      </div>
    </div>
  );
};

export default PromptInput;