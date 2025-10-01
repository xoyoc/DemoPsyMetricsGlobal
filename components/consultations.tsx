"use client"

import { useEffect, useRef, useState } from "react"
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card"
import { Button } from "@/components/ui/button"
import { Calendar, Video, MessageSquare, Clock } from "lucide-react"

export function Consultations() {
  const [isVisible, setIsVisible] = useState(false)
  const sectionRef = useRef<HTMLElement>(null)

  useEffect(() => {
    const observer = new IntersectionObserver(
      ([entry]) => {
        if (entry.isIntersecting) {
          setIsVisible(true)
        }
      },
      { threshold: 0.1 },
    )

    if (sectionRef.current) {
      observer.observe(sectionRef.current)
    }

    return () => observer.disconnect()
  }, [])

  const professionals = [
    {
      name: "Dra. Sarah Mitchell",
      role: "Psicóloga Organizacional",
      specialty: "Desarrollo de Liderazgo y Evaluación Ejecutiva",
      image: "/instructor.png",
      experience: "15+ años",
      availability: "Disponible para consulta",
    },
    {
      name: "Dr. James Chen",
      role: "Psicólogo Industrial",
      specialty: "Adquisición de Talento y Sistemas de Selección",
      image: "/professional-male-psychologist-headshot.jpg",
      experience: "12+ años",
      availability: "Disponible para consulta",
    },
    {
      name: "Dra. María Rodríguez",
      role: "Psicóloga Clínica",
      specialty: "Salud Mental y Bienestar Laboral",
      image: "/professional-female-clinical-psychologist-headshot.jpg",
      experience: "10+ años",
      availability: "Disponible para consulta",
    },
    {
      name: "Dr. David Thompson",
      role: "Psicólogo Cognitivo",
      specialty: "Evaluación Cognitiva y Análisis de Rendimiento",
      image: "/professional-male-cognitive-psychologist-headshot.jpg",
      experience: "18+ años",
      availability: "Disponible para consulta",
    },
  ]

  const consultationTypes = [
    {
      icon: Video,
      title: "Consulta por Video",
      description: "Sesiones virtuales individuales con nuestros expertos",
      duration: "60 minutos",
    },
    {
      icon: MessageSquare,
      title: "Revisión de Evaluación",
      description: "Análisis detallado e interpretación de resultados",
      duration: "45 minutos",
    },
    {
      icon: Calendar,
      title: "Planificación Estratégica",
      description: "Desarrollo de estrategia de talento a largo plazo",
      duration: "90 minutos",
    },
  ]

  return (
    <section id="consultations" ref={sectionRef} className="py-24 bg-muted/30">
      <div className="container mx-auto px-4 lg:px-8">
        <div
          className={`text-center max-w-3xl mx-auto mb-16 space-y-4 transition-all duration-1000 ${
            isVisible ? "opacity-100 translate-y-0" : "opacity-0 translate-y-8"
          }`}
        >
          <h2 className="text-sm font-semibold text-primary uppercase tracking-wider">Consultas Privadas</h2>
          <h3 className="text-4xl lg:text-5xl font-bold leading-tight text-balance">
            Orientación Experta de Profesionales Líderes
          </h3>
          <p className="text-lg text-muted-foreground leading-relaxed">
            Programe consultas privadas con nuestro equipo de psicólogos certificados y especialistas en RRHH para
            discutir las necesidades específicas de su organización.
          </p>
        </div>

        {/* Consultation Types */}
        <div className="grid md:grid-cols-3 gap-6 mb-16">
          {consultationTypes.map((type, index) => {
            const Icon = type.icon
            return (
              <Card
                key={index}
                className={`text-center transition-all duration-700 ${
                  isVisible ? "opacity-100 translate-y-0" : "opacity-0 translate-y-8"
                }`}
                style={{ transitionDelay: `${index * 100}ms` }}
              >
                <CardHeader>
                  <div className="h-16 w-16 rounded-full bg-primary/10 flex items-center justify-center mx-auto mb-4">
                    <Icon className="h-8 w-8 text-primary" />
                  </div>
                  <CardTitle className="text-xl">{type.title}</CardTitle>
                  <CardDescription>{type.description}</CardDescription>
                </CardHeader>
                <CardContent>
                  <div className="flex items-center justify-center text-sm text-muted-foreground">
                    <Clock className="h-4 w-4 mr-2" />
                    {type.duration}
                  </div>
                </CardContent>
              </Card>
            )
          })}
        </div>

        {/* Professionals Grid */}
        <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-6">
          {professionals.map((professional, index) => (
            <Card
              key={index}
              className={`group hover:shadow-xl transition-all duration-700 ${
                isVisible ? "opacity-100 translate-y-0" : "opacity-0 translate-y-8"
              }`}
              style={{ transitionDelay: `${(index + 3) * 100}ms` }}
            >
              <CardHeader className="p-0">
                <div className="aspect-square overflow-hidden rounded-t-lg">
                  <img
                    src={professional.image || "/placeholder.svg"}
                    alt={professional.name}
                    className="object-cover w-full h-full group-hover:scale-105 transition-transform duration-500"
                  />
                </div>
              </CardHeader>
              <CardContent className="p-6 space-y-3">
                <div>
                  <h4 className="font-bold text-lg">{professional.name}</h4>
                  <p className="text-sm text-primary font-medium">{professional.role}</p>
                </div>
                <p className="text-sm text-muted-foreground leading-relaxed">{professional.specialty}</p>
                <div className="pt-2 space-y-2">
                  <div className="text-xs text-muted-foreground">{professional.experience} de experiencia</div>
                  <div className="flex items-center text-xs text-accent">
                    <span className="h-2 w-2 rounded-full bg-accent mr-2 animate-pulse" />
                    {professional.availability}
                  </div>
                </div>
                <Button className="w-full mt-4" size="sm">
                  Reservar Consulta
                </Button>
              </CardContent>
            </Card>
          ))}
        </div>
      </div>
    </section>
  )
}
