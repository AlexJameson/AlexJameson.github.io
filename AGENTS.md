# AGENTS.md

This file provides guidance to agents when working with code in this repository.

## Build/lint/test commands

* `zola serve` - Run development server with live reload
* `zola build` - Build static site for production
* `zola check` - Validate site without building

## Code style guidelines

* Articles written in Russian with technical English terms
* Use GitHub Flavored Markdown with Zola extensions
* TOML front matter required for all articles with title, date, description, tags
* Mermaid diagrams supported with `{% mermaid() %}` shortcode
* Internal links use Zola's relative path format: `@/articles/filename.md`
* External links use absolute URLs
* Images referenced as: `![alt text](/assets/filename.png)`

## Project-specific patterns

* Content organized in `content/articles/` with TOML front matter
* Custom shortcodes in `templates/shortcodes/` for Mermaid diagrams and notes
* Sass styling with modular structure in `sass/` directory
* JavaScript enhancements in `static/js/` for interactivity
* Theme configuration in `config.toml` and `theme.toml`
* Custom macros in `templates/macros/macros.html` for content rendering
* Search functionality implemented with ElasticLunr
* Dark/light theme toggle with localStorage persistence

## Non-obvious gotchas

* Articles must include taxonomy tags for proper categorization
* Date format in front matter must be "YYYY-MM-DD"
* Mermaid diagrams require both `{% mermaid() %}` wrapper and standard mermaid syntax
* Internal links must use `@/` prefix for proper Zola resolution
* Custom fonts loaded locally from `static/fonts/` directory
* Theme switching requires both CSS files and JavaScript coordination