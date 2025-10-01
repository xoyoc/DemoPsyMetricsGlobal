"use client"

import { useEffect, useRef, useState } from "react"
import { CheckCircle2 } from "lucide-react"

export function About() {
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

  const features = [
    "Marcos psicológicos basados en evidencia",
    "Soluciones de evaluación personalizadas",
    "Informes y análisis en tiempo real",
    "Cumplimiento con estándares internacionales",
    "Capacidades de evaluación multilingüe",
    "Equipo de soporte dedicado",
  ]

  return (
    <section id="about" ref={sectionRef} className="py-24 bg-muted/30">
      <div className="container mx-auto px-4 lg:px-8">
        <div className="grid lg:grid-cols-2 gap-16 items-center">
          <div
            className={`transition-all duration-1000 ${
              isVisible ? "opacity-100 translate-x-0" : "opacity-0 -translate-x-8"
            }`}
          >
            <div className="relative aspect-[4/3] rounded-2xl overflow-hidden shadow-2xl">
              <img
                src="/modern-office-with-psychology-assessment-charts-an.jpg"
                alt="Análisis de evaluaciones"
                className="object-cover w-full h-full"
              />
            </div>
          </div>

          <div
            className={`space-y-6 transition-all duration-1000 delay-300 ${
              isVisible ? "opacity-100 translate-x-0" : "opacity-0 translate-x-8"
            }`}
          >
            <div className="space-y-4">
              <h2 className="text-sm font-semibold text-primary uppercase tracking-wider">
                Acerca de PsyMetrics Global
              </h2>
              <h3 className="text-4xl lg:text-5xl font-bold leading-tight text-balance">
                Transformando la Adquisición de Talento a Través de la Ciencia
              </h3>
            </div>

            <p className="text-lg text-muted-foreground leading-relaxed">
              Somos un colectivo de psicólogos organizacionales, científicos de datos y profesionales de RRHH dedicados
              a revolucionar cómo las empresas identifican, evalúan y desarrollan el talento. Nuestras evaluaciones
              científicamente validadas proporcionan información profunda sobre habilidades cognitivas, rasgos de
              personalidad y competencias conductuales.
            </p>

            <div className="grid sm:grid-cols-2 gap-4 pt-4">
              {features.map((feature, index) => (
                <div
                  key={index}
                  className="flex items-start space-x-3 animate-in fade-in slide-in-from-bottom-2"
                  style={{ animationDelay: `${index * 100}ms` }}
                >
                  <CheckCircle2 className="h-5 w-5 text-primary flex-shrink-0 mt-0.5" />
                  <span className="text-sm text-foreground">{feature}</span>
                </div>
              ))}
            </div>
          </div>
        </div>
      </div>
    </section>
  )
}
