"use client"

import { useEffect, useRef, useState } from "react"
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card"
import { Button } from "@/components/ui/button"
import { Brain, Users, Target, BarChart3, Shield, Zap } from "lucide-react"

export function Services() {
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

  const services = [
    {
      icon: Brain,
      title: "Evaluaciones Cognitivas",
      description:
        "Mida el pensamiento crítico, las habilidades de resolución de problemas y la capacidad intelectual con nuestra suite de pruebas cognitivas validadas.",
      features: ["Razonamiento lógico", "Aptitud numérica", "Comprensión verbal"],
    },
    {
      icon: Users,
      title: "Perfiles de Personalidad",
      description:
        "Comprenda patrones de comportamiento, estilos de trabajo y ajuste cultural a través de evaluaciones integrales de personalidad.",
      features: ["Rasgos Big Five", "Preferencias laborales", "Dinámicas de equipo"],
    },
    {
      icon: Target,
      title: "Potencial de Liderazgo",
      description:
        "Identifique futuros líderes con evaluaciones diseñadas para evaluar capacidades de gestión y pensamiento estratégico.",
      features: ["Toma de decisiones", "Inteligencia emocional", "Visión y estrategia"],
    },
    {
      icon: BarChart3,
      title: "Evaluación de Habilidades",
      description:
        "Evalúe habilidades técnicas y blandas con evaluaciones específicas adaptadas a los requisitos de su industria.",
      features: ["Competencia técnica", "Habilidades de comunicación", "Adaptabilidad"],
    },
    {
      icon: Shield,
      title: "Pruebas de Integridad",
      description:
        "Asegure la ética y confiabilidad en el lugar de trabajo con nuestras evaluaciones de integridad y honestidad diseñadas científicamente.",
      features: ["Juicio ético", "Indicadores de confiabilidad", "Evaluación de riesgos"],
    },
    {
      icon: Zap,
      title: "Soluciones Personalizadas",
      description:
        "Marcos de evaluación a medida diseñados específicamente para las necesidades únicas y la cultura de su organización.",
      features: ["Métricas personalizadas", "Específico de la industria", "Soluciones escalables"],
    },
  ]

  return (
    <section id="services" ref={sectionRef} className="py-24 bg-background">
      <div className="container mx-auto px-4 lg:px-8">
        <div
          className={`text-center max-w-3xl mx-auto mb-16 space-y-4 transition-all duration-1000 ${
            isVisible ? "opacity-100 translate-y-0" : "opacity-0 translate-y-8"
          }`}
        >
          <h2 className="text-sm font-semibold text-primary uppercase tracking-wider">Nuestros Servicios</h2>
          <h3 className="text-4xl lg:text-5xl font-bold leading-tight text-balance">
            Soluciones Integrales de Evaluación
          </h3>
          <p className="text-lg text-muted-foreground leading-relaxed">
            Nuestra colección de servicios de evaluación psicológica abarca diversas necesidades en cada etapa del
            proceso de gestión del talento.
          </p>
        </div>

        <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-6">
          {services.map((service, index) => {
            const Icon = service.icon
            return (
              <Card
                key={index}
                className={`group hover:shadow-xl transition-all duration-500 hover:-translate-y-1 ${
                  isVisible ? "opacity-100 translate-y-0" : "opacity-0 translate-y-8"
                }`}
                style={{ transitionDelay: `${index * 100}ms` }}
              >
                <CardHeader>
                  <div className="h-12 w-12 rounded-lg bg-primary/10 flex items-center justify-center mb-4 group-hover:bg-primary/20 transition-colors">
                    <Icon className="h-6 w-6 text-primary" />
                  </div>
                  <CardTitle className="text-xl">{service.title}</CardTitle>
                  <CardDescription className="text-base leading-relaxed">{service.description}</CardDescription>
                </CardHeader>
                <CardContent>
                  <ul className="space-y-2 mb-4">
                    {service.features.map((feature, idx) => (
                      <li key={idx} className="text-sm text-muted-foreground flex items-center">
                        <span className="h-1.5 w-1.5 rounded-full bg-primary mr-2" />
                        {feature}
                      </li>
                    ))}
                  </ul>
                  <Button variant="ghost" size="sm" className="w-full group-hover:bg-primary/10">
                    Conocer Más
                  </Button>
                </CardContent>
              </Card>
            )
          })}
        </div>
      </div>
    </section>
  )
}
