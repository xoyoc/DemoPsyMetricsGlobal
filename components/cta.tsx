"use client"

import { Button } from "@/components/ui/button"
import { ArrowRight, Mail, Phone } from "lucide-react"
import { useEffect, useRef, useState } from "react"

export function CTA() {
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

  return (
    <section id="contact" ref={sectionRef} className="py-24 bg-background">
      <div className="container mx-auto px-4 lg:px-8">
        <div
          className={`relative overflow-hidden rounded-3xl bg-gradient-to-br from-primary via-secondary to-primary p-12 lg:p-20 transition-all duration-1000 ${
            isVisible ? "opacity-100 scale-100" : "opacity-0 scale-95"
          }`}
        >
          {/* Background pattern */}
          <div className="absolute inset-0 opacity-10">
            <div className="absolute top-0 left-0 w-full h-full bg-[radial-gradient(circle_at_50%_50%,rgba(255,255,255,0.1),transparent_50%)]" />
          </div>

          <div className="relative z-10 max-w-3xl mx-auto text-center space-y-8">
            <h2 className="text-4xl lg:text-5xl font-bold text-primary-foreground leading-tight text-balance">
              ¿Listo para Transformar su Proceso de Contratación?
            </h2>
            <p className="text-xl text-primary-foreground/90 leading-relaxed">
              Únase a más de 200 organizaciones líderes que confían en PsyMetrics Global para sus necesidades de
              evaluación de talento. Hablemos sobre cómo podemos ayudarle a construir un equipo más sólido.
            </p>

            <div className="flex flex-col sm:flex-row gap-4 justify-center pt-4">
              <Button
                size="lg"
                variant="secondary"
                className="group bg-background text-foreground hover:bg-background/90"
              >
                Agendar una Demo
                <ArrowRight className="ml-2 h-4 w-4 group-hover:translate-x-1 transition-transform" />
              </Button>
              <Button
                size="lg"
                variant="outline"
                className="border-primary-foreground/20 text-primary-foreground hover:bg-primary-foreground/10 bg-transparent"
              >
                Contactar Ventas
              </Button>
            </div>

            <div className="flex flex-col sm:flex-row items-center justify-center gap-6 pt-8 text-primary-foreground/80">
              <a
                href="mailto:info@psymetricsglobal.com"
                className="flex items-center space-x-2 hover:text-primary-foreground transition-colors"
              >
                <Mail className="h-5 w-5" />
                <span>info@psymetricsglobal.com</span>
              </a>
              <a
                href="tel:+1234567890"
                className="flex items-center space-x-2 hover:text-primary-foreground transition-colors"
              >
                <Phone className="h-5 w-5" />
                <span>+1 (234) 567-890</span>
              </a>
            </div>
          </div>
        </div>
      </div>
    </section>
  )
}
