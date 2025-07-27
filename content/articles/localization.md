---
title: "Локализация чисел"
date: 2025-07-26
draft: false
---
# Интерактивный пример форматирования чисел для разных локалей

## Числа

<div class="localization-playground">
  <div class="formatting-form">
    <div class="input-group">
      <label for="number-input">Введите число:</label>
      <input type="text" id="number-input" placeholder="1234.56">
    </div>
    <div class="selector-group">
      <label for="locale-selector">Локаль:</label>
      <select id="locale-selector">
        <option value="ru-RU">Ru</option>
        <option value="en-US">En</option>
      </select>
    </div>
    <div class="output-group">
      <label for="formatted-output">Отформатированное число:</label>
      <div class="output-container">
        <input type="text" id="formatted-output" readonly>
        <button class="copy-button" aria-label="Копировать">
          <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect>
            <path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path>
          </svg>
        </button>
      </div>
    </div>
  </div>
  <div class="examples">
    <h4>Примеры форматирования</h4>
    <div class="example-item">
      <span class="example-label">Российская локаль (ru-RU):</span>
      <span class="example-value" data-locale="ru-RU">1 234,56</span>
    </div>
    <div class="example-item">
      <span class="example-label">Английская локаль (en-US):</span>
      <span class="example-value" data-locale="en-US">1,234.56</span>
    </div>
  </div>
</div>