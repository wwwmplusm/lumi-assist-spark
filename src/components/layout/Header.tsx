import { Link } from 'react-router-dom';
import { StudentHoverMenu } from './StudentHoverMenu';
import { Button } from '../ui/button';

export default function Header() {
  return (
    <header className="sticky top-0 z-50 w-full border-b bg-background/95 backdrop-blur supports-[backdrop-filter]:bg-background/60">
      <div className="container flex h-14 items-center">
        <Link to="/" className="mr-6 flex items-center space-x-2">
          <span className="font-bold">Lumi AI</span>
        </Link>
        <nav className="flex items-center space-x-6 text-sm font-medium">
          <StudentHoverMenu />
          <Link to="/library">
            <Button variant="link" className="text-foreground">Библиотека</Button>
          </Link>
        </nav>
      </div>
    </header>
  );
}
