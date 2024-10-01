Introduction: 

    Tailwind CSS is a utility-first CSS framework that provides low-level utility classes to help you build custom designs without having to write custom CSS. Instead of writing complex CSS rules, you can use predefined classes directly in your HTML to style elements.

How to use Tailwind css in projects 

    Testing : directly use tailwind cdn in html head section

        <script src="https://cdn.tailwindcss.com"></script>

        or
        
        <link href="/path/to/tailwind.css" rel="stylesheet">


    Production : 

        1. Install Tailwind CSS via npm:

            npm install -D tailwindcss
            npx tailwindcss init

            --> This will install Tailwind CSS and create a tailwind.config.js file for customization.

        2. Configure your template paths:
        
            Update the tailwind.config.js file to include the paths to your templates. 
            For example, if you have HTML and JavaScript files in a src directory, your configuration should look like this:

            module.exports = {
                content: [
                    './src/**/*.{html,js}',
                ],
                theme: {
                    extend: {},
                },
                plugins: [],
            }
        
        3. Add Tailwind to your CSS:

            Create a CSS file (e.g., styles.css)

            @tailwind base;
            @tailwind components;
            @tailwind utilities;

        4. Build your CSS:

            npx tailwindcss -i ./src/styles.css -o ./dist/output.css --watch

            --> This command watches your styles.css file and compiles it to output.css
