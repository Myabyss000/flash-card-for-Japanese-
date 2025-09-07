# 🎌 Japanese Flashcards App

An elegant, modern web application for learning Japanese Kanji characters with beautiful animations and interactive features.

![Japanese Flashcards](https://img.shields.io/badge/Japanese-Kanji-red?style=for-the-badge&logo=javascript)
![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)

## ✨ Features

- **100 N5 Level Kanji**: Comprehensive collection of essential Japanese kanji characters
- **Beautiful Glassmorphism Design**: Modern UI with glassmorphism effects and smooth animations
- **Intelligent Reading Classification**: Automatically separates on'yomi and kun'yomi readings with visual emphasis
- **Progress Tracking**: Local storage saves your learning progress
- **Responsive Design**: Optimized for desktop, tablet, and mobile devices
- **Interactive Animations**: Smooth hover effects, 3D transforms, and particle animations
- **Accessibility**: Semantic HTML and keyboard navigation support

## 🚀 Live Demo

[View Live Demo](https://your-username.github.io/japanese-flashcards) *(Replace with your actual GitHub Pages URL)*

## 📋 Prerequisites

- Modern web browser with JavaScript enabled
- Python 3.x (for local development server)

## 🛠️ Installation & Setup

### Option 1: GitHub Pages (Recommended for deployment)

1. Fork this repository
2. Go to Settings → Pages
3. Select "Deploy from a branch"
4. Choose "main" branch and "/ (root)" folder
5. Save and wait for deployment

### Option 2: Local Development

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/japanese-flashcards.git
   cd japanese-flashcards
   ```

2. **Start the development server**
   ```bash
   # Using npm
   npm start

   # Or directly with Python
   python server.py
   ```

3. **Open your browser**
   ```
   Navigate to: http://localhost:6000
   ```

## 🎯 Usage

1. **Browse Kanji**: Use Previous/Next buttons to navigate through kanji
2. **Reveal Answers**: Click "Show Answer" to see meanings and readings
3. **Track Progress**: Your progress is automatically saved locally
4. **Mobile Friendly**: Works perfectly on all device sizes

## 📁 Project Structure

```
japanese-flashcards/
├── index.html          # Main HTML structure
├── style.css          # Styling and animations
├── app.js            # Application logic
├── kanji.json        # Kanji data (100 N5 characters)
├── server.py         # Python development server
├── package.json      # Node.js configuration
├── .gitignore        # Git ignore rules
├── LICENSE          # MIT License
├── README.md        # Project documentation
├── CONTRIBUTING.md  # Contribution guidelines
├── .editorconfig    # Code style configuration
└── .github/
    └── workflows/
        └── ci-cd.yml    # GitHub Actions CI/CD
```

## 🛠️ Technologies Used

- **Frontend**: HTML5, CSS3, JavaScript (ES6+)
- **Styling**: Custom CSS with Glassmorphism effects
- **Fonts**: Google Fonts (Noto Sans JP, Poppins, JetBrains Mono)
- **Animations**: CSS Transforms, Keyframes, and Transitions
- **Storage**: Browser LocalStorage API
- **Server**: Python HTTP Server

## 🎨 Design Features

- **Glassmorphism UI**: Modern glass-like effects with backdrop blur
- **3D Animations**: Hover effects with perspective transforms
- **Particle System**: Floating animated particles in background
- **Gradient Backgrounds**: Dynamic color gradients
- **Responsive Typography**: Optimized for all screen sizes
- **Smooth Transitions**: Cubic-bezier easing functions

## 📊 Kanji Data Structure

Each kanji entry contains:
```json
{
  "kanji": "日",
  "meaning": "day, sun",
  "onyomi": ["ニチ", "ジツ"],
  "kunyomi": ["ひ", "か"]
}
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Kanji data sourced from reputable Japanese language learning resources
- Icons and animations inspired by modern web design trends
- Special thanks to the Japanese language learning community

## 📞 Contact

- **Author**: Your Name
- **GitHub**: [@your-username](https://github.com/your-username)
- **Email**: your.email@example.com

---

⭐ **Star this repo** if you found it helpful!

Made with ❤️ for Japanese language learners
