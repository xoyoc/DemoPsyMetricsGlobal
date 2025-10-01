"use client"

import { Button } from "@/components/ui/button"
import { ArrowRight, Brain, Users, TrendingUp } from "lucide-react"
import { useEffect, useState } from "react"

export function Hero() {
  const [isVisible, setIsVisible] = useState(false)

  useEffect(() => {
    setIsVisible(true)
  }, [])

  return (
    <section
      id="home"
      className="relative min-h-screen flex items-center justify-center overflow-hidden bg-gradient-to-br from-primary/5 via-background to-secondary/5"
    >
      {/* Animated background elements */}
      <div className="absolute inset-0 overflow-hidden">
        <div className="absolute top-1/4 left-1/4 w-96 h-96 bg-primary/10 rounded-full blur-3xl animate-pulse" />
        <div className="absolute bottom-1/4 right-1/4 w-96 h-96 bg-secondary/10 rounded-full blur-3xl animate-pulse delay-1000" />
      </div>

      <div className="container mx-auto px-4 lg:px-8 py-32 relative z-10">
        <div className="grid lg:grid-cols-2 gap-12 items-center">
          <div
            className={`space-y-8 transition-all duration-1000 ${
              isVisible ? "opacity-100 translate-y-0" : "opacity-0 translate-y-8"
            }`}
          >
            <div className="inline-block">
              <span className="px-4 py-2 bg-primary/10 text-primary rounded-full text-sm font-medium">
                Soluciones Líderes en Evaluación de RRHH
              </span>
            </div>

            <h1 className="text-5xl lg:text-7xl font-bold leading-tight text-balance">
              Donde la <span className="text-primary">Psicología</span> se Encuentra con la{" "}
              <span className="text-secondary">Excelencia Corporativa</span>
            </h1>

            <p className="text-xl text-muted-foreground leading-relaxed text-pretty">
              Empoderamos a las organizaciones con evaluaciones psicológicas científicamente validadas para tomar
              decisiones más inteligentes en reclutamiento, desarrollo y gestión del talento.
            </p>

            <div className="flex flex-col sm:flex-row gap-4">
              <Button size="lg" className="group">
                Agendar Evaluación
                <ArrowRight className="ml-2 h-4 w-4 group-hover:translate-x-1 transition-transform" />
              </Button>
              <Button size="lg" variant="outline">
                Conocer Más
              </Button>
            </div>

            <div className="grid grid-cols-3 gap-6 pt-8">
              <div className="space-y-2">
                <div className="flex items-center space-x-2 text-primary">
                  <Brain className="h-5 w-5" />
                  <span className="text-2xl font-bold">500+</span>
                </div>
                <p className="text-sm text-muted-foreground">Evaluaciones Realizadas</p>
              </div>
              <div className="space-y-2">
                <div className="flex items-center space-x-2 text-secondary">
                  <Users className="h-5 w-5" />
                  <span className="text-2xl font-bold">200+</span>
                </div>
                <p className="text-sm text-muted-foreground">Clientes Corporativos</p>
              </div>
              <div className="space-y-2">
                <div className="flex items-center space-x-2 text-accent">
                  <TrendingUp className="h-5 w-5" />
                  <span className="text-2xl font-bold">95%</span>
                </div>
                <p className="text-sm text-muted-foreground">Tasa de Éxito</p>
              </div>
            </div>
          </div>

          <div
            className={`relative transition-all duration-1000 delay-300 ${
              isVisible ? "opacity-100 translate-x-0" : "opacity-0 translate-x-8"
            }`}
          >
            <div className="relative aspect-square rounded-2xl overflow-hidden shadow-2xl">
              <img
                src="/professional-business-meeting-with-diverse-team-di.jpg"
                alt="Colaboración profesional del equipo"
                className="object-cover w-full h-full"
              />
              <div className="absolute inset-0 bg-gradient-to-t from-primary/20 to-transparent" />
            </div>

            {/* Floating cards */}
            <div className="absolute -bottom-6 -left-6 bg-card p-6 rounded-xl shadow-xl border border-border animate-in slide-in-from-bottom-4 delay-700">
              <div className="flex items-center space-x-3">
                <div className="h-12 w-12 rounded-full bg-primary/10 flex items-center justify-center">
                  <Brain className="h-6 w-6 text-primary" />
                </div>
                <div>
                  <p className="text-sm font-medium">Evaluaciones Validadas</p>
                  <p className="text-xs text-muted-foreground">Certificado ISO</p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  )
}
