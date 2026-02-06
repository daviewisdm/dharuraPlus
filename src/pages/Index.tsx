import { Phone, MapPin, Clock, Shield, Heart, Users } from "lucide-react";
import SOSButton from "@/components/SOSButton";
import FeatureCard from "@/components/FeatureCard";
import { toast } from "sonner";
import { Navbar } from "@/layout/Navbar";


const Index = () => {
  const handleSOSClick = () => {
    toast.error("Emergency SOS Activated!", {
      description: "Contacting emergency services and your emergency contacts...",
      duration: 5000,
    });
  };

  return (
    <div className="min-h-screen bg-background">

      <header className="fixed top-0 left-0 right-0 z-50 bg-background/80 backdrop-blur-md border-b border-border">
        <div className="container mx-auto px-4 py-4 flex items-center justify-between">
          <div className="flex items-center gap-2">
            <div className="w-10 h-10 rounded-xl bg-sos flex items-center justify-center">
              <Heart className="w-5 h-5 text-sos-foreground" />
            </div>
            <span className="text-xl font-bold text-foreground">DharuraPlus</span>
          </div>
          <nav className="hidden md:flex items-center gap-6">
            <a href="#features" className="text-muted-foreground hover:text-foreground transition-colors">
              Features
            </a>
            <a href="#how-it-works" className="text-muted-foreground hover:text-foreground transition-colors">
              How It Works
            </a>
            <a href="#contact" className="text-muted-foreground hover:text-foreground transition-colors">
              Contact
            </a>
            <a href="/about" className="text-muted-foreground hover:text-foreground transition-colors">
              About
            </a>
          </nav>
        </div>
      </header>





      {/* Hero Section */}
      <section className="pt-28 pb-16 md:pt-36 md:pb-24">
        <div className="container mx-auto px-4">
          <div className="flex flex-col items-center text-center">
            <span className="inline-flex items-center gap-2 px-4 py-2 rounded-full bg-primary/10 text-primary text-sm font-medium mb-6">
              <Shield className="w-4 h-4" />
              Your Safety, One Tap Away
            </span>

            <h1 className="text-4xl md:text-6xl font-bold text-foreground mb-6 text-balance max-w-3xl">
              Emergency Help When{" "}
              <span className="text-sos">Every Second</span> Counts
            </h1>

            <p className="text-lg md:text-xl text-muted-foreground max-w-2xl mb-12 text-balance">
              Dharura connects you instantly to emergency services and alerts your loved ones with your location. Be prepared for any health emergency.
            </p>

            {/* SOS Button */}
            <div className="relative mb-12">
              <SOSButton onClick={handleSOSClick} />
            </div>

            <p className="text-sm text-muted-foreground">
              Press the SOS button to immediately alert emergency services
            </p>
          </div>
        </div>
      </section>

      {/* Features Section */}
      <section id="features" className="py-16 md:py-24 bg-secondary/30">
        <div className="container mx-auto px-4">
          <div className="text-center mb-12">
            <h2 className="text-3xl md:text-4xl font-bold text-foreground mb-4">
              Why Choose DharuraPlus?
            </h2>
            <p className="text-muted-foreground max-w-xl mx-auto">
              Comprehensive emergency response features designed to save lives
            </p>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 max-w-5xl mx-auto">
            <FeatureCard
              icon={Phone}
              title="One-Tap SOS"
              description="Instantly connect to emergency services with a single tap. No fumbling, no delays."
            />
            <FeatureCard
              icon={MapPin}
              title="Location Sharing"
              description="Your precise location is shared automatically with responders and emergency contacts."
            />
            <FeatureCard
              icon={Clock}
              title="24/7 Monitoring"
              description="Round-the-clock monitoring ensures help is always just a tap away."
            />
            <FeatureCard
              icon={Users}
              title="Emergency Contacts"
              description="Alert your family and friends simultaneously when you need help."
            />
            <FeatureCard
              icon={Heart}
              title="Medical Profile"
              description="Store vital medical info accessible to first responders for better care."
            />
            <FeatureCard
              icon={Shield}
              title="Fall Detection"
              description="Automatic alerts when a fall is detected, even if you can't press the button."
            />
          </div>
        </div>
      </section>

      {/* How It Works */}
      <section id="how-it-works" className="py-16 md:py-24">
        <div className="container mx-auto px-4">
          <div className="text-center mb-12">
            <h2 className="text-3xl md:text-4xl font-bold text-foreground mb-4">
              How It Works
            </h2>
            <p className="text-muted-foreground max-w-xl mx-auto">
              Simple, fast, and reliable emergency response in three steps
            </p>
          </div>

          <div className="flex flex-col md:flex-row items-center justify-center gap-8 md:gap-16 max-w-4xl mx-auto">
            <div className="flex flex-col items-center text-center">
              <div className="w-16 h-16 rounded-full bg-sos/10 text-sos flex items-center justify-center text-2xl font-bold mb-4">
                1
              </div>
              <h3 className="text-lg font-semibold text-foreground mb-2">Press SOS</h3>
              <p className="text-muted-foreground text-sm max-w-48">
                Tap the SOS button when you need immediate help
              </p>
            </div>

            <div className="hidden md:block w-16 h-0.5 bg-border" />

            <div className="flex flex-col items-center text-center">
              <div className="w-16 h-16 rounded-full bg-primary/10 text-primary flex items-center justify-center text-2xl font-bold mb-4">
                2
              </div>
              <h3 className="text-lg font-semibold text-foreground mb-2">We Alert</h3>
              <p className="text-muted-foreground text-sm max-w-48">
                Emergency services and your contacts are notified instantly
              </p>
            </div>

            <div className="hidden md:block w-16 h-0.5 bg-border" />

            <div className="flex flex-col items-center text-center">
              <div className="w-16 h-16 rounded-full bg-trust/10 text-trust flex items-center justify-center text-2xl font-bold mb-4">
                3
              </div>
              <h3 className="text-lg font-semibold text-foreground mb-2">Help Arrives</h3>
              <p className="text-muted-foreground text-sm max-w-48">
                Help locate you using your shared location
              </p>
            </div>
          </div>
        </div>
      </section>

      {/* CTA Section */}
      <section className="py-16 md:py-24 bg-primary text-primary-foreground">
        <div className="container mx-auto px-4 text-center">
          <h2 className="text-3xl md:text-4xl font-bold mb-4">
            Ready to stay safe?
          </h2>
          <p className="text-primary-foreground/80 max-w-xl mx-auto mb-8">
            Join thousands who trust Dharura to keep them and their loved ones safe.
          </p>
          <button className="px-8 py-4 bg-sos text-sos-foreground rounded-xl font-semibold hover:opacity-90 transition-opacity shadow-lg">
            Get Started Free
          </button>
        </div>
      </section>

      {/* Footer */}
      <footer id="contact" className="py-12 border-t border-border">
        <div className="container mx-auto px-4">
          <div className="flex flex-col md:flex-row items-center justify-between gap-6">
            <div className="flex items-center gap-2">
              <div className="w-8 h-8 rounded-lg bg-sos flex items-center justify-center">
                <Heart className="w-4 h-4 text-sos-foreground" />
              </div>
              <span className="text-lg font-bold text-foreground">DharuraAi</span>
            </div>

            <p className="text-muted-foreground text-sm">
              Emergency: <a href="tel:911" className="text-sos font-semibold hover:underline">911</a>
            </p>

            <p className="text-muted-foreground text-sm">
              © 2026 Dharura. All rights reserved.
            </p>
          </div>
        </div>
      </footer>
    </div>
  );
};

export default Index;
