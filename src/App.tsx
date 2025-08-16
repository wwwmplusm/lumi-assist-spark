import { BrowserRouter, Routes, Route, Outlet } from 'react-router-dom';
import Header from '@/components/layout/Header';
import Dashboard from '@/pages/Dashboard';
import StudentProfile from '@/pages/StudentProfile';
import Library from '@/pages/Library';

const AppLayout = () => (
  <div className="min-h-screen bg-background text-foreground">
    <Header />
    <main>
      <Outlet />
    </main>
  </div>
);

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<AppLayout />}>
          <Route index element={<Dashboard />} />
          <Route path="students/:studentId" element={<StudentProfile />} />
          <Route path="library" element={<Library />} />
        </Route>
      </Routes>
    </BrowserRouter>
  );
}

export default App;
