# Stage 1: Base image with Python
FROM python:3.12-slim as base

# Stage 2: Builder stage with uv
FROM base AS builder
# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

# Set environment variables
ENV UV_COMPILE_BYTECODE=1
ENV UV_LINK_MODE=copy

# Set working directory
WORKDIR /app

# Copy project files for dependency installation
COPY uv.lock pyproject.toml /app/

# Install dependencies using uv with caching
# RUN --mount=type=cache,target=/root/.cache/uv \
#     uv sync --frozen --no-install-project --no-dev
RUN uv sync --frozen --no-install-project --no-dev

# Copy the rest of the application code
COPY .python-version script.sh /app/
COPY src /app/src/

# Install project dependencies
# RUN --mount=type=cache,target=/root/.cache/uv \
#     uv sync --frozen --no-dev

RUN uv sync --frozen --no-dev

# Stage 3: Final image
FROM base

# Copy dependencies and application code from builder stage
COPY --from=builder /app /app

# Set the PATH to include the virtual environment
ENV PATH="/app/.venv/bin:$PATH"

# Expose the application port
EXPOSE 8000

# Command to run the application
CMD ["bash","script.sh"]