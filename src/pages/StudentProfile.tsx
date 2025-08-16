import { useParams } from 'react-router-dom';
import { useStudentStore } from '@/store/studentStore';
import { Avatar, AvatarFallback, AvatarImage } from "@/components/ui/avatar";
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Plus, Upload, Dribbble } from "lucide-react";
import { HoverCard, HoverCardContent, HoverCardTrigger } from '@/components/ui/hover-card';

// Вкладка "Главная"
const MainTab = () => (
  <div className="space-y-6">
    <Card><CardHeader><CardTitle>Текущая домашняя работа на 27.07</CardTitle></CardHeader><CardContent><ul className="list-disc list-inside space-y-2"><li className="cursor-pointer hover:underline">жи-ши практика</li><li className="cursor-pointer hover:underline">видеоурок "как найти суффикс в слове?"</li></ul></CardContent></Card>
    <Card><CardHeader><CardTitle>Неоцененное Д/З</CardTitle></CardHeader><CardContent><p className="text-muted-foreground">Все задания проверены!</p></CardContent></Card>
    <Button className="fixed bottom-8 right-8 h-14 px-6 rounded-full shadow-lg"><Plus className="mr-2" />Задать домашнее задание</Button>
  </div>
);

// Вкладка "Материалы"
const MaterialsTab = () => (
  <div>
    <Card><CardHeader><CardTitle>Список материалов</CardTitle></CardHeader><CardContent>Здесь будут материалы...</CardContent></Card>
    <HoverCard><HoverCardTrigger asChild><Button className="fixed bottom-8 right-8 h-14 px-6 rounded-full shadow-lg"><Plus className="mr-2" />Добавить материалы</Button></HoverCardTrigger><HoverCardContent side="top" className="w-60"><div className="flex flex-col space-y-1"><Button variant="ghost"><Upload className="mr-2 h-4 w-4" />Добавить файлы</Button><Button variant="ghost"><Dribbble className="mr-2 h-4 w-4" />Из Google Drive</Button></div></HoverCardContent></HoverCard>
  </div>
);

// Вкладка "Оцененные"
const GradedTab = () => (
  <div className="space-y-4">
    <Card><CardContent className="p-4 flex justify-between items-center"><span>Задание 14 ЕГЭ</span><strong>10/10</strong></CardContent></Card>
    <Card><CardContent className="p-4 flex justify-between items-center"><span>Задание 15 ЕГЭ русский</span><strong>42/45</strong></CardContent></Card>
  </div>
);

export default function StudentProfile() {
  const { studentId } = useParams<{ studentId: string }>();
  const student = useStudentStore((s) => s.students.find(st => st.id === studentId));

  if (!student) return <div className="container p-8">Ученик не найден...</div>;

  return (
    <div>
      <header className="sticky top-14 z-10 border-b bg-background/80 backdrop-blur-sm">
        <div className="container flex items-center space-x-4 p-4 h-24">
          <Avatar className="h-16 w-16"><AvatarImage src={`https://api.dicebear.com/8.x/initials/svg?seed=${student.name}`} /><AvatarFallback>{student.name.slice(0, 2)}</AvatarFallback></Avatar>
          <div>
            <h1 className="text-2xl font-bold">{student.name}</h1>
            <p className="text-muted-foreground">{student.email || 'Русский язык'}</p>
          </div>
        </div>
      </header>
      <div className="container p-4">
        <Tabs defaultValue="main" className="w-full">
          <TabsList><TabsTrigger value="main">Главная</TabsTrigger><TabsTrigger value="materials">Материалы</TabsTrigger><TabsTrigger value="graded">Оцененные Д/З</TabsTrigger></TabsList>
          <TabsContent value="main"><MainTab /></TabsContent>
          <TabsContent value="materials"><MaterialsTab /></TabsContent>
          <TabsContent value="graded"><GradedTab /></TabsContent>
        </Tabs>
      </div>
    </div>
  );
}
