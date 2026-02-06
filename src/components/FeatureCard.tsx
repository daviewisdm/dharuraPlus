import { cn } from "@/lib/utils";
import { LucideIcon } from "lucide-react";

interface FeatureCardProps {
  icon: LucideIcon;
  title: string;
  description: string;
  className?: string;
}

const FeatureCard = ({ icon: Icon, title, description, className }: FeatureCardProps) => {
  return (
    <div
      className={cn(
        "flex flex-col items-center text-center p-6 rounded-2xl",
        "bg-card border border-border/50",
        "hover:shadow-card hover:border-primary/20",
        "transition-all duration-300",
        className
      )}
    >
      <div className="w-14 h-14 rounded-xl bg-primary/10 flex items-center justify-center mb-4">
        <Icon className="w-7 h-7 text-primary" />
      </div>
      <h3 className="text-lg font-semibold text-foreground mb-2">{title}</h3>
      <p className="text-muted-foreground text-sm leading-relaxed">{description}</p>
    </div>
  );
};

export default FeatureCard;
