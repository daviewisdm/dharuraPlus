import { cn } from "@/lib/utils";

interface SOSButtonProps {
  onClick?: () => void;
  className?: string;
}

const SOSButton = ({ onClick, className }: SOSButtonProps) => {
  return (
    <button
      onClick={onClick}
      className={cn(
        "relative flex items-center justify-center",
        "w-48 h-48 md:w-56 md:h-56",
        "rounded-full bg-sos text-sos-foreground",
        "text-4xl md:text-5xl font-bold tracking-wider",
        "shadow-sos hover:shadow-sos-hover",
        "transform hover:scale-105 active:scale-95",
        "transition-all duration-200",
        "focus:outline-none focus:ring-4 focus:ring-sos/50",
        className
      )}
    >
      {/* Pulse rings */}
      <span className="absolute inset-0 rounded-full bg-sos/30 animate-ping-slow" />
      <span className="absolute inset-2 rounded-full bg-sos/20 animate-ping-slower" />
      
      {/* Button content */}
      <span className="relative z-10">SOS</span>
    </button>
  );
};

export default SOSButton;
