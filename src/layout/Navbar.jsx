import { Button } from "@/components/Button";
import { Menu, X } from "lucide-react";
import { useEffect, useState } from "react";

const navLinks = [
    { href: "#features", label: "features" },
    { href: "#how-it-works", label: "howitworks" },
    { href: "#contact", label: "contact" },


];

export const Navbar = () => {
    const [isMobileMenuOpen, setIsMobileMenuOpen] = useState(false);
    const [isScrolled, setIsScrolled] = useState(false);

    useEffect(() => {
        const handleScroll = () => {
            setIsScrolled(window.scrollY > 50);
        };

        window.addEventListener("scroll", handleScroll);

        return () => window.removeEventListener("scroll", handleScroll);
    }, []);

    return (
        <header
            className={`fixed top-0 left-0 right-0 transition-all duration-500 ${isScrolled ? "glass-strong py-3" : "bg-transparent py-5"
                }  z-50`}
        >
            <nav className="container mx-auto px-6 flex items-center justify-between">
                <a
                    href="#"
                    className="text-xl font-bold tracking-tight hover:text-primary"
                >
                    <div className="w-10 h-10 rounded-xl bg-sos flex items-center justify-center">
                        <Heart className="w-5 h-5 text-sos-foreground" />
                    </div> <span className=" hover:text-primary">Dharura</span> <span className="text-primary hover:text-primary-foreground">Plus</span>
                </a>

                {/* Desktop Nav */}
                <div className="hidden md:flex items-center gap-1  ">
                    <div className="glass rounded-full px-2 py-1 flex items-center gap-1">
                        {navLinks.map((link, index) => (
                            <a
                                href={link.href}
                                key={index}
                                className="px-4 py-2 text-sm text-muted-foreground hover:text-foreground rounded-full hover:bg-primary"
                            >
                                {link.label}
                            </a>
                        ))}
                    </div>
                </div>

                {/* CTA Button  */}
                <div className="hidden md:block">
                    <a href="#contact">
                        <Button size="sm">Contact Me</Button>
                    </a>
                </div>


                {/* Mobile Menu Button */}
                <button
                    className="md:hidden p-2 text-foreground cursor-pointer"
                    onClick={() => setIsMobileMenuOpen((prev) => !prev)}
                >
                    {isMobileMenuOpen ? <X size={24} /> : <Menu size={24} />}
                </button>
            </nav>

            {/* Mobile Menu */}
            {isMobileMenuOpen && (
                <div className="md:hidden glass-strong animate-fade-in">
                    <div className="container mx-auto px-6 py-6 flex flex-col gap-4">
                        {navLinks.map((link, index) => (
                            <a
                                href={link.href}
                                key={index}
                                onClick={() => setIsMobileMenuOpen(false)}
                                className="text-lg text-muted-foreground hover:text-foreground py-2"
                            >
                                {link.label}
                            </a>
                        ))}

                        <a href="#contact">
                            <Button onClick={() => setIsMobileMenuOpen(false)}>
                                Contact Me
                            </Button>
                        </a>


                    </div>
                </div>
            )}
        </header>
    );
};