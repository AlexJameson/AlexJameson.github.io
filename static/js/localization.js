document.addEventListener('DOMContentLoaded', function() {
    const numberInput = document.getElementById('number-input');
    const formattedOutput = document.getElementById('formatted-output');
    const localeSelector = document.getElementById('locale-selector');
    const copyButton = document.querySelector('.copy-button');
    const exampleValues = document.querySelectorAll('.example-value');

    // Format number based on selected locale
    function formatNumber() {
        const inputValue = numberInput.value.trim();
        
        // Clear output if input is empty
        if (!inputValue) {
            formattedOutput.value = '';
            return;
        }
        
        // Parse input to number
        const number = parseFloat(inputValue.replace(/[^0-9.-]/g, ''));
        
        // Check if it's a valid number
        if (isNaN(number)) {
            formattedOutput.value = 'Недопустимое число';
            return;
        }
        
        // Get selected locale
        const locale = localeSelector.value;
        
        // Format number using Intl.NumberFormat
        try {
            const formatter = new Intl.NumberFormat(locale, {
                minimumFractionDigits: 2,
                maximumFractionDigits: 2
            });
            formattedOutput.value = formatter.format(number);
        } catch (error) {
            formattedOutput.value = 'Ошибка форматирования';
        }
    }

    // Update formatting when input changes or locale changes
    numberInput.addEventListener('input', formatNumber);
    localeSelector.addEventListener('change', formatNumber);

    // Copy functionality
    copyButton.addEventListener('click', function() {
        if (formattedOutput.value && formattedOutput.value !== 'Недопустимое число' && formattedOutput.value !== 'Ошибка форматирования') {
            navigator.clipboard.writeText(formattedOutput.value).then(() => {
                // Visual feedback
                copyButton.classList.add('copied');
                setTimeout(() => {
                    copyButton.classList.remove('copied');
                }, 2000);
            }).catch(err => {
                console.error('Could not copy text: ', err);
            });
        }
    });

    // Initialize with empty output
    formattedOutput.value = '';
    
    // Update examples when locale changes
    function updateExamples() {
        const locale = localeSelector.value;
        exampleValues.forEach(example => {
            const value = example.getAttribute('data-locale') === 'ru-RU' ? 1234.56 : 1234.56;
            const formatter = new Intl.NumberFormat(example.getAttribute('data-locale'), {
                minimumFractionDigits: 2,
                maximumFractionDigits: 2
            });
            example.textContent = formatter.format(value);
        });
    }
    
    // Initialize examples
    updateExamples();
    localeSelector.addEventListener('change', updateExamples);
});