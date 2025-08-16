import React, { useEffect } from 'react';
import { Link } from 'react-router-dom';
import { useStudentStore } from '@/store/studentStore';
import { HoverCard, HoverCardContent, HoverCardTrigger } from "@/components/ui/hover-card";
import { Button } from "@/components/ui/button";
import { Avatar, AvatarFallback } from "@/components/ui/avatar";

export function StudentHoverMenu() {
  const { students, fetchStudents } = useStudentStore();

  useEffect(() => {
    // Загружаем студентов при первом рендере компонента
    fetchStudents();
  }, [fetchStudents]);

  return (
    <HoverCard>
      <HoverCardTrigger asChild>
        <Button variant="link" className="text-foreground">Ученики</Button>
      </HoverCardTrigger>
      <HoverCardContent className="w-80">
        <div className="flex flex-col space-y-1">
          <h4 className="font-medium">Список учеников</h4>
          {students.map((student) => (
            <Link key={student.id} to={`/students/${student.id}`} className="block p-2 rounded-md hover:bg-secondary">
              <div className="flex items-center space-x-3">
                <Avatar><AvatarFallback>{student.name.slice(0, 2)}</AvatarFallback></Avatar>
                <p className="text-sm font-medium">{student.name}</p>
              </div>
            </Link>
          ))}
        </div>
      </HoverCardContent>
    </HoverCard>
  );
}
