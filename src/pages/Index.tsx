import HamburgerMenu from '../components/HamburgerMenu';
import Sidebar from '../components/Sidebar';
import PromptInput from '../components/PromptInput';
import { createNewAssignment } from '../services/api';

const Index = () => {
  const handleCreateTestAssignment = async () => {
    try {
      console.log('Creating new assignment...');
      const newAssignment = await createNewAssignment('My Test Assignment');
      console.log('Successfully created assignment:', newAssignment);
      alert(`Assignment created with ID: ${newAssignment.assignment_id}`);
    } catch (error) {
      console.error('Error creating assignment:', error);
      alert('Failed to create assignment. Check the console.');
    }
  };

  return (
    <div className="min-h-screen tech-grid-bg relative overflow-hidden">
      <HamburgerMenu />
      <Sidebar />
      <div className="min-h-screen flex flex-col items-center justify-center px-4">
        <div className="text-center max-w-4xl">
          <h1 className="text-5xl md:text-6xl lg:text-7xl font-bold neon-glow mb-8 leading-tight">
            Lumi AI — ваш главный помощник в сфере образования
          </h1>
          <button
            onClick={handleCreateTestAssignment}
            className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
          >
            Test Create Assignment API
          </button>
        </div>
      </div>
      <PromptInput />
    </div>
  );
};

export default Index;
