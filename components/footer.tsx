import Link from "next/link"
import { Linkedin, Twitter, Facebook, Mail } from "lucide-react"

export function Footer() {
  const footerLinks = {
    company: [
      { label: "Nosotros", href: "#about" },
      { label: "Nuestro Equipo", href: "#team" },
      { label: "Carreras", href: "#careers" },
      { label: "Prensa", href: "#press" },
    ],
    services: [
      { label: "Evaluaciones Cognitivas", href: "#services" },
      { label: "Perfiles de Personalidad", href: "#services" },
      { label: "Potencial de Liderazgo", href: "#services" },
      { label: "Soluciones Personalizadas", href: "#services" },
    ],
    resources: [
      { label: "Artículos de Investigación", href: "#research" },
      { label: "Casos de Estudio", href: "#cases" },
      { label: "Blog", href: "#blog" },
      { label: "Preguntas Frecuentes", href: "#faq" },
    ],
    legal: [
      { label: "Política de Privacidad", href: "#privacy" },
      { label: "Términos de Servicio", href: "#terms" },
      { label: "Protección de Datos", href: "#data" },
      { label: "Cumplimiento", href: "#compliance" },
    ],
  }

  return (
    <footer className="bg-primary text-primary-foreground">
      <div className="container mx-auto px-4 lg:px-8 py-16">
        <div className="grid md:grid-cols-2 lg:grid-cols-6 gap-12 mb-12">
          <div className="lg:col-span-2 space-y-4">
            <div className="flex items-center space-x-2">
              <div className="text-2xl font-bold">PsyMetrics</div>
              <div className="text-2xl font-light">Global</div>
            </div>
            <p className="text-primary-foreground/80 leading-relaxed text-pretty">
              Empoderamos a las organizaciones con evaluaciones psicológicas científicamente validadas para decisiones
              de talento más inteligentes.
            </p>
            <div className="flex space-x-4">
              <a
                href="#"
                className="h-10 w-10 rounded-full bg-primary-foreground/10 flex items-center justify-center hover:bg-primary-foreground/20 transition-colors"
                aria-label="LinkedIn"
              >
                <Linkedin className="h-5 w-5" />
              </a>
              <a
                href="#"
                className="h-10 w-10 rounded-full bg-primary-foreground/10 flex items-center justify-center hover:bg-primary-foreground/20 transition-colors"
                aria-label="Twitter"
              >
                <Twitter className="h-5 w-5" />
              </a>
              <a
                href="#"
                className="h-10 w-10 rounded-full bg-primary-foreground/10 flex items-center justify-center hover:bg-primary-foreground/20 transition-colors"
                aria-label="Facebook"
              >
                <Facebook className="h-5 w-5" />
              </a>
              <a
                href="#"
                className="h-10 w-10 rounded-full bg-primary-foreground/10 flex items-center justify-center hover:bg-primary-foreground/20 transition-colors"
                aria-label="Email"
              >
                <Mail className="h-5 w-5" />
              </a>
            </div>
          </div>

          <div>
            <h3 className="font-semibold mb-4">Empresa</h3>
            <ul className="space-y-3">
              {footerLinks.company.map((link) => (
                <li key={link.href}>
                  <Link
                    href={link.href}
                    className="text-sm text-primary-foreground/80 hover:text-primary-foreground transition-colors"
                  >
                    {link.label}
                  </Link>
                </li>
              ))}
            </ul>
          </div>

          <div>
            <h3 className="font-semibold mb-4">Servicios</h3>
            <ul className="space-y-3">
              {footerLinks.services.map((link) => (
                <li key={link.href}>
                  <Link
                    href={link.href}
                    className="text-sm text-primary-foreground/80 hover:text-primary-foreground transition-colors"
                  >
                    {link.label}
                  </Link>
                </li>
              ))}
            </ul>
          </div>

          <div>
            <h3 className="font-semibold mb-4">Recursos</h3>
            <ul className="space-y-3">
              {footerLinks.resources.map((link) => (
                <li key={link.href}>
                  <Link
                    href={link.href}
                    className="text-sm text-primary-foreground/80 hover:text-primary-foreground transition-colors"
                  >
                    {link.label}
                  </Link>
                </li>
              ))}
            </ul>
          </div>

          <div>
            <h3 className="font-semibold mb-4">Legal</h3>
            <ul className="space-y-3">
              {footerLinks.legal.map((link) => (
                <li key={link.href}>
                  <Link
                    href={link.href}
                    className="text-sm text-primary-foreground/80 hover:text-primary-foreground transition-colors"
                  >
                    {link.label}
                  </Link>
                </li>
              ))}
            </ul>
          </div>
        </div>

        <div className="pt-8 border-t border-primary-foreground/10">
          <div className="flex flex-col md:flex-row justify-between items-center gap-4">
            <p className="text-sm text-primary-foreground/60">
              © 2025 PsyMetrics Global. Todos los derechos reservados.
            </p>
            <p className="text-sm text-primary-foreground/60">Certificado ISO 9001:2015 | Acreditado por APA</p>
          </div>
        </div>
      </div>
    </footer>
  )
}
