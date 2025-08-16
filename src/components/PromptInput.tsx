import { Plus, Upload, CloudDownload } from 'lucide-react';
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuTrigger,
} from '@/components/ui/dropdown-menu';
import { Button } from '@/components/ui/button';
import { Input } from '@/components/ui/input';

const PromptInput = () => {
  return (
    <div className="fixed bottom-6 left-1/2 -translate-x-1/2 w-full max-w-2xl px-4">
      <div className="relative">
        <Input
          type="text"
          placeholder="Что вы хотите создать сегодня?"
          className="w-full px-6 py-4 pr-16 h-14 rounded-full text-lg focus:ring-2 focus:ring-blue-400 transition-all bg-white text-black placeholder:text-gray-500"
        />
        <div className="absolute right-3 top-1/2 -translate-y-1/2">
          <DropdownMenu>
            <DropdownMenuTrigger asChild>
              <Button
                variant="default"
                size="icon"
                className="w-10 h-10 bg-black rounded-full hover:bg-gray-800"
              >
                <Plus size={20} className="text-white" />
              </Button>
            </DropdownMenuTrigger>
            <DropdownMenuContent className="w-64 mb-2" side="top" align="end">
              <DropdownMenuItem onSelect={() => console.log('Upload files clicked')}>
                <Upload className="mr-2 h-4 w-4" />
                <span>добавить файлы и фотографии</span>
              </DropdownMenuItem>
              <DropdownMenuItem onSelect={() => console.log('Google Drive clicked')}>
                <CloudDownload className="mr-2 h-4 w-4" />
                <span>добавить из Google Drive</span>
              </DropdownMenuItem>
            </DropdownMenuContent>
          </DropdownMenu>
        </div>
      </div>
    </div>
  );
};

export default PromptInput;

