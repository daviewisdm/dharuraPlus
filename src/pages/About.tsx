// src/pages/About.tsx
import React from "react";
import { Users, Target, Eye, Mail } from "lucide-react";

const About: React.FC = () => {
    return (
        <div className="bg-gray-50 min-h-screen">
            {/* Hero Section */}
            <div className="bg-primary text-white py-16 px-6 text-center">
                <h1 className="text-4xl md:text-5xl font-bold mb-4">About DharuraPlus</h1>
                <p className="text-lg md:text-xl max-w-2xl mx-auto">
                    Innovating digital solutions for students and professionals to stay organized, productive, and informed.
                </p>
            </div>

            {/* Main Content */}
            <div className="max-w-6xl mx-auto p-6 grid gap-8 md:grid-cols-2">
                {/* Mission */}
                <div className="bg-white p-6 rounded-xl shadow-lg hover:shadow-xl transition-shadow duration-300">
                    <div className="flex items-center mb-4 text-primary">
                        <Target className="w-6 h-6 mr-2" />
                        <h2 className="text-2xl font-semibold">Our Mission</h2>
                    </div>
                    <p className="text-gray-700">
                        Empowering students and professionals by delivering intuitive digital tools that streamline learning, organization, and communication.
                    </p>
                </div>

                {/* Vision */}
                <div className="bg-white p-6 rounded-xl shadow-lg hover:shadow-xl transition-shadow duration-300">
                    <div className="flex items-center mb-4 text-primary">
                        <Eye className="w-6 h-6 mr-2" />
                        <h2 className="text-2xl font-semibold">Our Vision</h2>
                    </div>
                    <p className="text-gray-700">
                        To be a leading tech platform bridging education and technology, making learning and productivity accessible to everyone.
                    </p>
                </div>

                {/* Team */}
                <div className="bg-white p-6 rounded-xl shadow-lg hover:shadow-xl transition-shadow duration-300">
                    <div className="flex items-center mb-4 text-primary">
                        <Users className="w-6 h-6 mr-2" />
                        <h2 className="text-2xl font-semibold">Our Team</h2>
                    </div>
                    <p className="text-gray-700">
                        Passionate developers, designers, and innovators committed to building software that users love. Collaboration, creativity, and continuous learning are at our core.
                    </p>
                </div>

                {/* Contact */}
                <div className="bg-white p-6 rounded-xl shadow-lg hover:shadow-xl transition-shadow duration-300">
                    <div className="flex items-center mb-4 text-primary">
                        <Mail className="w-6 h-6 mr-2" />
                        <h2 className="text-2xl font-semibold">Get In Touch</h2>
                    </div>
                    <p className="text-gray-700">
                        Have questions or suggestions? Reach out at{" "}
                        <span className="font-medium text-primary">contact@dharuraplus.com</span>.
                    </p>
                </div>
            </div>

            {/* Optional Footer CTA */}
            <div className="bg-primary/10 py-12 text-center mt-12">
                <h3 className="text-2xl md:text-3xl font-bold mb-4">Join Our Journey</h3>
                <p className="text-gray-700 mb-6 max-w-xl mx-auto">
                    Be part of our community and stay updated on our latest tools, apps, and innovations!
                </p>
                <button className="bg-primary text-white px-6 py-3 rounded-lg font-semibold hover:bg-primary/90 transition">
                    Subscribe
                </button>
            </div>
        </div>
    );
};

export default About;
