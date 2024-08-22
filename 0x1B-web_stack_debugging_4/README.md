# Web Stack Debugging #4 🚀

Welcome to the fourth installment in the web stack debugging series! This project marks the fifth time I’ve rolled up my sleeves to tackle broken or bugged web stacks, each housed in its own isolated container. My mission? To bring these web stacks back to life, restoring them to a fully functional state. Each task required careful analysis, troubleshooting, and a sprinkle of automation magic to ensure that everything worked seamlessly again.

## Overview 🛠️

In this project, I was tasked with solving two critical issues related to web server performance and user configuration. To achieve this, I crafted Puppet manifests that automated the necessary fixes, ensuring that the web stack could handle the load and users could log in without a hitch.

### Tasks 📃

#### 0. Sky is the Limit, Let's Bring That Limit Higher 🌤️

- **File:** `0-the_sky_is_the_limit_not.pp`
- **Description:** This Puppet manifest was designed to push the boundaries of what our Apache web server could handle. By fine-tuning the server configuration, I was able to significantly increase the amount of traffic the server could manage without buckling under pressure.

#### 1. User Limit 🚦

- **File:** `1-user_limit.pp`
- **Description:** In this task, the goal was to eliminate a pesky operating system limitation that was preventing the `holberton` user from logging in and opening files. With this Puppet manifest, I reconfigured the OS to lift the file descriptor limits, allowing seamless access for the user.

## Project Highlights 🌟

- **Automation:** Each task was automated using Puppet, ensuring that the fixes were not only effective but also reproducible.
- **Debugging Excellence:** This project honed my debugging skills, pushing me to identify and resolve complex issues within the web stack.
- **Scalability:** The improvements made in the first task have a direct impact on the scalability of the web server, making it more resilient under high traffic conditions.

## How to Use 🛠️

1. Clone this repository:
    ```bash
    git clone https://github.com/JohnSamy2004/alx-system_engineering-devops.git
    ```
2. Navigate to the project directory:
    ```bash
    cd alx-system_engineering-devops/0x1B-web_stack_debugging_4
    ```
3. Apply the Puppet manifests:
    ```bash
    sudo puppet apply 0-the_sky_is_the_limit_not.pp
    sudo puppet apply 1-user_limit.pp
    ```

## Final Thoughts 💭

This project was a deep dive into the intricacies of web stack management and debugging. By automating the resolution of critical issues, I’ve not only restored functionality but also ensured that the web stack is more robust and scalable than ever before. This experience has been invaluable in sharpening my skills in both system administration and automation.

---

Feel free to explore the project, run the scripts, and see the results for yourself. Happy debugging! 🎉


