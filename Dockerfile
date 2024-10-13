# Use the official Rust image with Python and GCC pre-installed
FROM rust:1.72-slim

# Install Python virtual environment tools, GCC, and necessary packages
RUN apt-get update && apt-get install -y \
    python3 python3-pip python3-venv gcc build-essential \
    && apt-get clean

# Set the working directory inside the container
WORKDIR /app

# Create the virtual environment and install Python dependencies
RUN python3 -m venv /app/venv
RUN /app/venv/bin/pip install numpy scipy

# Set CMD to execute commands step-by-step with informative prints
CMD echo "Compiling C program..." && \
    gcc random_generator.c -o random_generator_c && \
    echo "C program compiled. Done." && \
    echo "Building Rust program..." && \
    cd random_generator && cargo build --release && cd .. && \
    echo "Rust program built. Done." && \
    echo "Copying Rust binary to /app..." && \
    cp random_generator/target/release/random_generator /app/random_generator_rust && \
    echo "Rust binary copied. Done." && \
    echo "Running Python experiment..." && \
    /app/venv/bin/python experiment.py && \
    echo "Python experiment completed. Done."

# docker build -t experiment-env .
# docker run --rm -v "$(pwd)":/app -w /app experiment-env