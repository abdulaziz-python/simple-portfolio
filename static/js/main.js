// Mobile Navigation Toggle
document.addEventListener("DOMContentLoaded", () => {
  const navToggle = document.getElementById("nav-toggle")
  const navMenu = document.getElementById("nav-menu")

  if (navToggle && navMenu) {
    navToggle.addEventListener("click", () => {
      navMenu.classList.toggle("active")
      window.PortfolioApp.animateHamburger(navToggle)
    })

    // Close menu when clicking on a link
    const navLinks = document.querySelectorAll(".nav-link")
    navLinks.forEach((link) => {
      link.addEventListener("click", () => {
        navMenu.classList.remove("active")
        window.PortfolioApp.resetHamburger(navToggle)
      })
    })

    // Close menu when clicking outside
    document.addEventListener("click", (e) => {
      if (!navToggle.contains(e.target) && !navMenu.contains(e.target)) {
        navMenu.classList.remove("active")
        window.PortfolioApp.resetHamburger(navToggle)
      }
    })
  }
})

// Smooth scrolling for anchor links
document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
  anchor.addEventListener("click", function (e) {
    e.preventDefault()
    const target = document.querySelector(this.getAttribute("href"))
    if (target) {
      target.scrollIntoView({
        behavior: "smooth",
        block: "start",
      })
    }
  })
})

// Add scroll effect to navbar
window.addEventListener("scroll", () => {
  const navbar = document.querySelector(".navbar")
  const scrolled = window.scrollY > 100

  if (scrolled) {
    navbar.style.background = "rgba(255, 255, 255, 0.98)"
    navbar.style.boxShadow = "0 2px 20px rgba(0, 0, 0, 0.1)"
  } else {
    navbar.style.background = "rgba(255, 255, 255, 0.95)"
    navbar.style.boxShadow = "none"
  }

  // Parallax effect for hero section
  const hero = document.querySelector(".hero")
  if (hero) {
    const scrolled = window.pageYOffset
    const rate = scrolled * -0.5
    hero.style.transform = `translateY(${rate}px)`
  }

  // Progress indicator
  window.PortfolioApp.updateScrollProgress()
})

// Animate elements on scroll
const observerOptions = {
  threshold: 0.1,
  rootMargin: "0px 0px -50px 0px",
}

const observer = new IntersectionObserver((entries) => {
  entries.forEach((entry) => {
    if (entry.isIntersecting) {
      entry.target.classList.add("animate-in")

      // Add stagger effect for multiple elements
      if (entry.target.classList.contains("stagger-item")) {
        const delay = Array.from(entry.target.parentNode.children).indexOf(entry.target) * 100
        setTimeout(() => {
          entry.target.style.opacity = "1"
          entry.target.style.transform = "translateY(0)"
        }, delay)
      }
    }
  })
}, observerOptions)

// Observe elements for animation
document.addEventListener("DOMContentLoaded", () => {
  const animateElements = document.querySelectorAll(".project-card, .skill-item, .timeline-item")

  animateElements.forEach((el) => {
    el.style.opacity = "0"
    el.style.transform = "translateY(30px)"
    el.style.transition = "opacity 0.6s ease, transform 0.6s ease"
    observer.observe(el)
  })
})

// Form validation and submission
function validateForm(form) {
  const inputs = form.querySelectorAll("input[required], textarea[required]")
  let isValid = true

  inputs.forEach((input) => {
    const value = input.value.trim()
    const isEmail = input.type === "email"

    if (!value || (isEmail && !isValidEmail(value))) {
      isValid = false
      input.style.borderColor = "#dc3545"
      input.classList.add("error")
    } else {
      input.style.borderColor = "#28a745"
      input.classList.remove("error")
    }
  })

  return isValid
}

function isValidEmail(email) {
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/
  return emailRegex.test(email)
}

// Add loading state to buttons
function setButtonLoading(button, loading = true) {
  if (loading) {
    button.disabled = true
    button.innerHTML = '<div class="loading"></div> Sending...'
  } else {
    button.disabled = false
    button.innerHTML = '<i class="fas fa-paper-plane"></i> Send Message'
  }
}

// Copy to clipboard functionality
function copyToClipboard(text) {
  navigator.clipboard
    .writeText(text)
    .then(() => {
      showNotification("Copied to clipboard!", "success")
    })
    .catch(() => {
      showNotification("Failed to copy to clipboard.", "error")
    })
}

// Show notification
function showNotification(message, type = "info") {
  // Remove existing notifications
  document.querySelectorAll(".notification").forEach((n) => n.remove())

  const notification = document.createElement("div")
  notification.className = `notification notification-${type}`
  notification.innerHTML = `
    <div class="notification-content">
      <i class="fas fa-${getNotificationIcon(type)}"></i>
      <span>${message}</span>
      <button class="notification-close">&times;</button>
    </div>
  `

  notification.style.cssText = `
    position: fixed;
    top: 20px;
    right: 20px;
    background: var(--tertiary-bg);
    color: var(--primary-text);
    padding: 1rem 1.5rem;
    border-radius: var(--border-radius);
    box-shadow: var(--shadow-secondary);
    border-left: 4px solid var(--${type === "success" ? "success" : type === "error" ? "error" : "accent"}-color);
    z-index: 9999;
    animation: slideInRight 0.3s ease;
    max-width: 400px;
  `

  document.body.appendChild(notification)

  // Auto remove after 5 seconds
  setTimeout(() => {
    if (notification.parentNode) {
      notification.style.animation = "slideOutRight 0.3s ease"
      setTimeout(() => notification.remove(), 300)
    }
  }, 5000)

  // Manual close
  notification.querySelector(".notification-close").addEventListener("click", () => {
    notification.style.animation = "slideOutRight 0.3s ease"
    setTimeout(() => notification.remove(), 300)
  })
}

// Get notification icon
function getNotificationIcon(type) {
  const icons = {
    success: "check-circle",
    error: "exclamation-circle",
    warning: "exclamation-triangle",
    info: "info-circle",
  }
  return icons[type] || icons.info
}

// Dark mode toggle (optional feature)
function toggleDarkMode() {
  document.body.classList.toggle("dark-mode")
  localStorage.setItem("darkMode", document.body.classList.contains("dark-mode"))
}

// Load dark mode preference
document.addEventListener("DOMContentLoaded", () => {
  if (localStorage.getItem("darkMode") === "true") {
    document.body.classList.add("dark-mode")
  }
})

// Performance optimization: Debounce scroll events
function debounce(func, wait) {
  let timeout
  return function executedFunction(...args) {
    const later = () => {
      clearTimeout(timeout)
      func(...args)
    }
    clearTimeout(timeout)
    timeout = setTimeout(later, wait)
  }
}

// Apply debounce to scroll handler
const debouncedScrollHandler = debounce(() => {
  const navbar = document.querySelector(".navbar")
  const scrolled = window.scrollY > 100

  if (scrolled) {
    navbar.style.background = "rgba(255, 255, 255, 0.98)"
    navbar.style.boxShadow = "0 2px 20px rgba(0, 0, 0, 0.1)"
  } else {
    navbar.style.background = "rgba(255, 255, 255, 0.95)"
    navbar.style.boxShadow = "none"
  }
}, 10)

window.addEventListener("scroll", debouncedScrollHandler)

// Additional utility functions
const utils = {
  // Format date
  formatDate: (date) => {
    return new Intl.DateTimeFormat("en-US", {
      year: "numeric",
      month: "long",
      day: "numeric",
    }).format(new Date(date))
  },

  // Truncate text
  truncateText: (text, length = 100) => {
    return text.length > length ? text.substring(0, length) + "..." : text
  },

  // Generate random color
  randomColor: () => {
    const colors = ["#58a6ff", "#7ee787", "#d2a8ff", "#ffa657", "#f85149"]
    return colors[Math.floor(Math.random() * colors.length)]
  },

  // Check if element is in viewport
  isInViewport: (element) => {
    const rect = element.getBoundingClientRect()
    return (
      rect.top >= 0 &&
      rect.left >= 0 &&
      rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
      rect.right <= (window.innerWidth || document.documentElement.clientWidth)
    )
  },
}

// Export for use in other scripts
window.PortfolioUtils = utils

// Enhanced Portfolio JavaScript with Developer Environment Features

class PortfolioApp {
  constructor() {
    this.init()
    this.setupEventListeners()
    this.setupAnimations()
    this.setupTheme()
    this.setupTypingAnimation()
    this.setupTerminalEffects()
  }

  init() {
    // Initialize app
    this.isLoading = false
    this.currentTheme = localStorage.getItem("theme") || "dark"
    this.setTheme(this.currentTheme)

    // Setup intersection observer for animations
    this.setupIntersectionObserver()

    // Setup smooth scrolling
    this.setupSmoothScrolling()

    // Setup mobile navigation
    this.setupMobileNav()
  }

  setupEventListeners() {
    // Theme toggle
    const themeToggle = document.getElementById("theme-toggle")
    if (themeToggle) {
      themeToggle.addEventListener("click", () => this.toggleTheme())
    }

    // Scroll effects
    window.addEventListener(
      "scroll",
      this.debounce(() => {
        this.handleScroll()
      }, 10),
    )

    // Form submission
    const contactForm = document.getElementById("contact-form")
    if (contactForm) {
      contactForm.addEventListener("submit", (e) => this.handleFormSubmit(e))
    }

    // Copy to clipboard functionality
    document.querySelectorAll("[data-copy]").forEach((element) => {
      element.addEventListener("click", () => this.copyToClipboard(element.dataset.copy))
    })

    // Keyboard shortcuts
    document.addEventListener("keydown", (e) => this.handleKeyboardShortcuts(e))
  }

  setupAnimations() {
    // Setup GSAP animations if available
    if (typeof window.gsap !== "undefined") {
      this.setupGSAPAnimations()
    } else {
      this.setupCSSAnimations()
    }
  }

  setupIntersectionObserver() {
    const observerOptions = {
      threshold: 0.1,
      rootMargin: "0px 0px -50px 0px",
    }

    this.observer = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add("animate-in")

          // Add stagger effect for multiple elements
          if (entry.target.classList.contains("stagger-item")) {
            const delay = Array.from(entry.target.parentNode.children).indexOf(entry.target) * 100
            setTimeout(() => {
              entry.target.style.opacity = "1"
              entry.target.style.transform = "translateY(0)"
            }, delay)
          }
        }
      })
    }, observerOptions)

    // Observe elements
    document.querySelectorAll(".animate-on-scroll").forEach((el) => {
      el.style.opacity = "0"
      el.style.transform = "translateY(30px)"
      el.style.transition = "opacity 0.6s ease, transform 0.6s ease"
      this.observer.observe(el)
    })
  }

  setupSmoothScrolling() {
    document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
      anchor.addEventListener("click", (e) => {
        e.preventDefault()
        const target = document.querySelector(anchor.getAttribute("href"))
        if (target) {
          target.scrollIntoView({
            behavior: "smooth",
            block: "start",
          })
        }
      })
    })
  }

  setupMobileNav() {
    const navToggle = document.getElementById("nav-toggle")
    const navMenu = document.getElementById("nav-menu")

    if (navToggle && navMenu) {
      navToggle.addEventListener("click", () => {
        navMenu.classList.toggle("active")
        this.animateHamburger(navToggle)
      })

      // Close menu when clicking on links
      document.querySelectorAll(".nav-link").forEach((link) => {
        link.addEventListener("click", () => {
          navMenu.classList.remove("active")
          this.resetHamburger(navToggle)
        })
      })

      // Close menu when clicking outside
      document.addEventListener("click", (e) => {
        if (!navToggle.contains(e.target) && !navMenu.contains(e.target)) {
          navMenu.classList.remove("active")
          this.resetHamburger(navToggle)
        }
      })
    }
  }

  animateHamburger(toggle) {
    const bars = toggle.querySelectorAll(".bar")
    bars[0].style.transform = "rotate(-45deg) translate(-5px, 6px)"
    bars[1].style.opacity = "0"
    bars[2].style.transform = "rotate(45deg) translate(-5px, -6px)"
  }

  resetHamburger(toggle) {
    const bars = toggle.querySelectorAll(".bar")
    bars[0].style.transform = "none"
    bars[1].style.opacity = "1"
    bars[2].style.transform = "none"
  }

  setupTheme() {
    document.documentElement.setAttribute("data-theme", this.currentTheme)
  }

  toggleTheme() {
    this.currentTheme = this.currentTheme === "dark" ? "light" : "dark"
    this.setTheme(this.currentTheme)
    localStorage.setItem("theme", this.currentTheme)
  }

  setTheme(theme) {
    document.documentElement.setAttribute("data-theme", theme)

    // Update theme toggle icon
    const themeToggle = document.getElementById("theme-toggle")
    if (themeToggle) {
      const icon = themeToggle.querySelector("i")
      if (icon) {
        icon.className = theme === "dark" ? "fas fa-sun" : "fas fa-moon"
      }
    }
  }

  setupTypingAnimation() {
    const typingElements = document.querySelectorAll(".typing-text")

    typingElements.forEach((element) => {
      const text = element.textContent
      element.textContent = ""
      element.classList.add("typing-animation")

      let i = 0
      const typeWriter = () => {
        if (i < text.length) {
          element.textContent += text.charAt(i)
          i++
          setTimeout(typeWriter, 100)
        } else {
          element.classList.remove("typing-animation")
        }
      }

      // Start typing when element is visible
      const observer = new IntersectionObserver((entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            setTimeout(typeWriter, 500)
            observer.unobserve(entry.target)
          }
        })
      })

      observer.observe(element)
    })
  }

  setupTerminalEffects() {
    // Terminal typing effect
    const terminals = document.querySelectorAll(".terminal-content")

    terminals.forEach((terminal) => {
      const commands = [
        "$ whoami",
        "abdulaziz-hamidjonov",
        "$ ls -la skills/",
        "drwxr-xr-x  python/",
        "drwxr-xr-x  django/",
        "drwxr-xr-x  tensorflow/",
        "drwxr-xr-x  docker/",
        "$ cat about.txt",
        "AI/ML & Backend Developer",
        "Passionate about creating innovative solutions",
        "$ python --version",
        "Python 3.11.0",
        "$ git status",
        "On branch main",
        "Your branch is up to date",
        '$ echo "Ready to build amazing things!"',
        "Ready to build amazing things!",
      ]

      let commandIndex = 0
      let charIndex = 0

      const typeCommand = () => {
        if (commandIndex < commands.length) {
          const currentCommand = commands[commandIndex]

          if (charIndex < currentCommand.length) {
            terminal.textContent += currentCommand.charAt(charIndex)
            charIndex++
            setTimeout(typeCommand, 50)
          } else {
            terminal.textContent += "\n"
            commandIndex++
            charIndex = 0
            setTimeout(typeCommand, 1000)
          }
        }
      }

      // Start terminal animation when visible
      const observer = new IntersectionObserver((entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            setTimeout(typeCommand, 1000)
            observer.unobserve(entry.target)
          }
        })
      })

      observer.observe(terminal)
    })
  }

  handleScroll() {
    const navbar = document.querySelector(".navbar")
    const scrolled = window.scrollY > 100

    if (scrolled) {
      navbar.style.background = this.currentTheme === "dark" ? "rgba(13, 17, 23, 0.98)" : "rgba(255, 255, 255, 0.98)"
      navbar.style.boxShadow = "0 2px 20px rgba(0, 0, 0, 0.1)"
    } else {
      navbar.style.background = this.currentTheme === "dark" ? "rgba(13, 17, 23, 0.95)" : "rgba(255, 255, 255, 0.95)"
      navbar.style.boxShadow = "none"
    }

    // Parallax effect for hero section
    const hero = document.querySelector(".hero")
    if (hero) {
      const scrolled = window.pageYOffset
      const rate = scrolled * -0.5
      hero.style.transform = `translateY(${rate}px)`
    }

    // Progress indicator
    this.updateScrollProgress()
  }

  updateScrollProgress() {
    const winScroll = document.body.scrollTop || document.documentElement.scrollTop
    const height = document.documentElement.scrollHeight - document.documentElement.clientHeight
    const scrolled = (winScroll / height) * 100

    let progressBar = document.querySelector(".scroll-progress")
    if (!progressBar) {
      progressBar = document.createElement("div")
      progressBar.className = "scroll-progress"
      progressBar.style.cssText = `
        position: fixed;
        top: 0;
        left: 0;
        width: ${scrolled}%;
        height: 3px;
        background: linear-gradient(135deg, #58a6ff 0%, #a5a6ff 50%, #d2a8ff 100%);
        z-index: 9999;
        transition: width 0.1s ease;
      `
      document.body.appendChild(progressBar)
    } else {
      progressBar.style.width = scrolled + "%"
    }
  }

  async handleFormSubmit(e) {
    e.preventDefault()

    if (this.isLoading) return

    const form = e.target
    const formData = new FormData(form)
    const data = Object.fromEntries(formData)
    const submitBtn = form.querySelector('button[type="submit"]')

    // Validate form
    if (!this.validateForm(form)) {
      this.showNotification("Please fill in all required fields.", "error")
      return
    }

    this.setButtonLoading(submitBtn, true)
    this.isLoading = true

    try {
      const response = await fetch(form.action || "/contact/submit/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(data),
      })

      const result = await response.json()

      if (result.success) {
        this.showNotification(result.message, "success")
        form.reset()
        this.addSuccessAnimation(form)
      } else {
        this.showNotification(result.message, "error")
      }
    } catch (error) {
      this.showNotification("Sorry, there was an error sending your message. Please try again.", "error")
    } finally {
      this.setButtonLoading(submitBtn, false)
      this.isLoading = false
    }
  }

  validateForm(form) {
    const inputs = form.querySelectorAll("input[required], textarea[required]")
    let isValid = true

    inputs.forEach((input) => {
      const value = input.value.trim()
      const isEmail = input.type === "email"

      if (!value || (isEmail && !this.isValidEmail(value))) {
        isValid = false
        input.style.borderColor = "var(--error-color)"
        input.classList.add("error")
      } else {
        input.style.borderColor = "var(--success-color)"
        input.classList.remove("error")
      }
    })

    return isValid
  }

  isValidEmail(email) {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/
    return emailRegex.test(email)
  }

  setButtonLoading(button, loading = true) {
    if (loading) {
      button.disabled = true
      button.innerHTML = '<div class="loading"></div> Sending...'
    } else {
      button.disabled = false
      button.innerHTML = '<i class="fas fa-paper-plane"></i> Send Message'
    }
  }

  addSuccessAnimation(form) {
    form.style.transform = "scale(0.98)"
    form.style.opacity = "0.8"

    setTimeout(() => {
      form.style.transform = "scale(1)"
      form.style.opacity = "1"
    }, 200)
  }

  showNotification(message, type = "info") {
    // Remove existing notifications
    document.querySelectorAll(".notification").forEach((n) => n.remove())

    const notification = document.createElement("div")
    notification.className = `notification notification-${type}`
    notification.innerHTML = `
      <div class="notification-content">
        <i class="fas fa-${this.getNotificationIcon(type)}"></i>
        <span>${message}</span>
        <button class="notification-close">&times;</button>
      </div>
    `

    notification.style.cssText = `
      position: fixed;
      top: 20px;
      right: 20px;
      background: var(--tertiary-bg);
      color: var(--primary-text);
      padding: 1rem 1.5rem;
      border-radius: var(--border-radius);
      box-shadow: var(--shadow-secondary);
      border-left: 4px solid var(--${type === "success" ? "success" : type === "error" ? "error" : "accent"}-color);
      z-index: 9999;
      animation: slideInRight 0.3s ease;
      max-width: 400px;
    `

    document.body.appendChild(notification)

    // Auto remove after 5 seconds
    setTimeout(() => {
      if (notification.parentNode) {
        notification.style.animation = "slideOutRight 0.3s ease"
        setTimeout(() => notification.remove(), 300)
      }
    }, 5000)

    // Manual close
    notification.querySelector(".notification-close").addEventListener("click", () => {
      notification.style.animation = "slideOutRight 0.3s ease"
      setTimeout(() => notification.remove(), 300)
    })
  }

  getNotificationIcon(type) {
    const icons = {
      success: "check-circle",
      error: "exclamation-circle",
      warning: "exclamation-triangle",
      info: "info-circle",
    }
    return icons[type] || icons.info
  }

  copyToClipboard(text) {
    navigator.clipboard
      .writeText(text)
      .then(() => {
        this.showNotification("Copied to clipboard!", "success")
      })
      .catch(() => {
        this.showNotification("Failed to copy to clipboard.", "error")
      })
  }

  handleKeyboardShortcuts(e) {
    // Ctrl/Cmd + K for search (if implemented)
    if ((e.ctrlKey || e.metaKey) && e.key === "k") {
      e.preventDefault()
      // Implement search functionality
    }

    // Ctrl/Cmd + D for theme toggle
    if ((e.ctrlKey || e.metaKey) && e.key === "d") {
      e.preventDefault()
      this.toggleTheme()
    }

    // Escape to close mobile menu
    if (e.key === "Escape") {
      const navMenu = document.getElementById("nav-menu")
      if (navMenu && navMenu.classList.contains("active")) {
        navMenu.classList.remove("active")
        this.resetHamburger(document.getElementById("nav-toggle"))
      }
    }
  }

  setupGSAPAnimations() {
    // GSAP animations for enhanced effects
    window.gsap.registerPlugin(window.ScrollTrigger)

    // Hero animation
    window.gsap
      .timeline()
      .from(".hero-text", { duration: 1, y: 50, opacity: 0, ease: "power2.out" })
      .from(".hero-image", { duration: 1, x: 50, opacity: 0, ease: "power2.out" }, "-=0.5")

    // Skills animation
    window.gsap.from(".skill-item", {
      duration: 0.8,
      y: 30,
      opacity: 0,
      stagger: 0.1,
      ease: "power2.out",
      scrollTrigger: {
        trigger: ".skills-grid",
        start: "top 80%",
      },
    })

    // Projects animation
    window.gsap.from(".project-card", {
      duration: 0.8,
      y: 50,
      opacity: 0,
      stagger: 0.2,
      ease: "power2.out",
      scrollTrigger: {
        trigger: ".projects-grid",
        start: "top 80%",
      },
    })
  }

  setupCSSAnimations() {
    // Fallback CSS animations
    const style = document.createElement("style")
    style.textContent = `
      @keyframes slideInRight {
        from {
          transform: translateX(100%);
          opacity: 0;
        }
        to {
          transform: translateX(0);
          opacity: 1;
        }
      }
      
      @keyframes slideOutRight {
        from {
          transform: translateX(0);
          opacity: 1;
        }
        to {
          transform: translateX(100%);
          opacity: 0;
        }
      }
      
      .notification-content {
        display: flex;
        align-items: center;
        gap: 0.75rem;
      }
      
      .notification-close {
        background: none;
        border: none;
        color: var(--secondary-text);
        cursor: pointer;
        font-size: 1.2rem;
        margin-left: auto;
      }
      
      .notification-close:hover {
        color: var(--primary-text);
      }
    `
    document.head.appendChild(style)
  }

  debounce(func, wait) {
    let timeout
    return function executedFunction(...args) {
      const later = () => {
        clearTimeout(timeout)
        func(...args)
      }
      clearTimeout(timeout)
      timeout = setTimeout(later, wait)
    }
  }
}

// Initialize the app when DOM is loaded
document.addEventListener("DOMContentLoaded", () => {
  window.portfolioApp = new PortfolioApp()
})
