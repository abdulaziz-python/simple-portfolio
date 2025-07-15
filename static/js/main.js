// Mobile Navigation Toggle
document.addEventListener("DOMContentLoaded", () => {
  const navToggle = document.getElementById("nav-toggle")
  const navMenu = document.getElementById("nav-menu")

  if (navToggle && navMenu) {
    navToggle.addEventListener("click", () => {
      navMenu.classList.toggle("active")
    })

    // Close menu when clicking on a link
    const navLinks = document.querySelectorAll(".nav-link")
    navLinks.forEach((link) => {
      link.addEventListener("click", () => {
        navMenu.classList.remove("active")
      })
    })

    // Close menu when clicking outside
    document.addEventListener("click", (e) => {
      if (!navToggle.contains(e.target) && !navMenu.contains(e.target)) {
        navMenu.classList.remove("active")
      }
    })
  }

  // Theme toggle
  const themeToggle = document.getElementById("theme-toggle")
  const themeText = document.getElementById("theme-text")

  if (themeToggle) {
    // Load saved theme
    const savedTheme = localStorage.getItem("theme") || "light"
    document.body.setAttribute("data-theme", savedTheme)
    themeText.textContent = savedTheme === "light" ? "Dark" : "Light"

    themeToggle.addEventListener("click", () => {
      const currentTheme = document.body.getAttribute("data-theme")
      const newTheme = currentTheme === "light" ? "dark" : "light"

      document.body.setAttribute("data-theme", newTheme)
      themeText.textContent = newTheme === "light" ? "Dark" : "Light"
      localStorage.setItem("theme", newTheme)
    })
  }

  // Contact form submission
  const contactForm = document.getElementById("contact-form")
  if (contactForm) {
    contactForm.addEventListener("submit", async (e) => {
      e.preventDefault()

      const formData = new FormData(contactForm)
      const data = Object.fromEntries(formData)
      const submitBtn = contactForm.querySelector('button[type="submit"]')

      // Simple validation
      if (!data.name || !data.email || !data.subject || !data.message) {
        showNotification("Please fill in all fields.", "error")
        return
      }

      // Email validation
      const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/
      if (!emailRegex.test(data.email)) {
        showNotification("Please enter a valid email address.", "error")
        return
      }

      // Disable button
      submitBtn.disabled = true
      submitBtn.textContent = "Sending..."

      try {
        const response = await fetch(contactForm.action, {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(data),
        })

        const result = await response.json()

        if (result.success) {
          showNotification(result.message, "success")
          contactForm.reset()
        } else {
          showNotification(result.message, "error")
        }
      } catch (error) {
        showNotification("Error sending message. Please try again.", "error")
      } finally {
        submitBtn.disabled = false
        submitBtn.textContent = "Send Message"
      }
    })
  }
})

// Simple notification system
function showNotification(message, type = "info") {
  // Remove existing notifications
  document.querySelectorAll(".notification").forEach((n) => n.remove())

  const notification = document.createElement("div")
  notification.className = `notification notification-${type}`
  notification.innerHTML = `
        ${message}
        <button class="notification-close">&times;</button>
    `

  document.body.appendChild(notification)

  // Auto remove after 5 seconds
  setTimeout(() => {
    if (notification.parentNode) {
      notification.remove()
    }
  }, 5000)

  // Manual close
  notification.querySelector(".notification-close").addEventListener("click", () => {
    notification.remove()
  })
}

// Smooth scrolling for anchor links
document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
  anchor.addEventListener("click", function (e) {
    e.preventDefault()
    const target = document.querySelector(this.getAttribute("href"))
    if (target) {
      target.scrollIntoView({
        behavior: "smooth",
      })
    }
  })
})
