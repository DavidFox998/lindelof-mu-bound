CC = gcc
CFLAGS = -O3 -Wall -std=c99 -lm
TARGET = mu_sieve
PYTHON = python3

# BATTLE PLAN v1.6: FIREWALL - All targets depend on verify
all: verify $(TARGET)

$(TARGET): mu_sieve.c
	$(CC) $(CFLAGS) mu_sieve.c -o $(TARGET)

# Firewall target - must pass before any compilation
verify:
	@echo "=== LINDELÖF PLATFORM ANCHOR CHECK ==="
	$(PYTHON) verify.py
	@echo "=== ANCHOR VERIFIED: BUILD AUTHORIZED ==="

# Run test with σ=0.5
test: verify $(TARGET)
	./$(TARGET) 0.5

# Clean build artifacts
clean:
	rm -f $(TARGET)

.PHONY: all clean test verify
