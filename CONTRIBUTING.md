# Contributing to MAST Computer Vision Module

Thank you for your interest in contributing to the MAST Computer Vision Module! This document provides guidelines for contributing to this educational project.

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [Contributing Process](#contributing-process)
- [Coding Standards](#coding-standards)
- [Testing Guidelines](#testing-guidelines)
- [Documentation](#documentation)

## Code of Conduct

This project follows a simple code of conduct:
- Be respectful and inclusive
- Focus on educational value
- Help others learn
- Provide constructive feedback
- Follow academic integrity principles

## Getting Started

1. **Fork the repository** on GitHub
2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/your-username/MAST_learn.git
   cd MAST_learn
   ```
3. **Add upstream remote**:
   ```bash
   git remote add upstream https://github.com/lozingaro/MAST_learn.git
   ```

## Development Setup

### Prerequisites
- Python 3.8+ (3.8.5 recommended for Mind+ compatibility)
- Mind+ Desktop App (for testing blocks)
- Git for version control

### Environment Setup
```bash
# Create virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r python/libraries/requirements.txt
```

### Testing Setup
```bash
# Test basic functionality
python -c "from python.libraries.learn import capture_webcam_image; print('✓ Module loads successfully')"
```

## Contributing Process

### 1. Create Feature Branch
```bash
git checkout -b feature/your-feature-name
```

### 2. Make Changes
- Keep commits focused and atomic
- Write clear commit messages
- Test your changes thoroughly

### 3. Commit Guidelines
Follow this format for commit messages:
```
type: brief description

Longer description if necessary

- List specific changes
- Reference issues if applicable
```

Types: `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`

### 4. Submit Pull Request
1. Push your branch to your fork
2. Create a Pull Request with:
   - Clear title and description
   - Reference to related issues
   - Screenshots/examples if applicable
   - Test results

## Coding Standards

### Python Code Style
- Follow [PEP 8](https://pep8.org/) style guide
- Use 4 spaces for indentation
- Maximum line length: 88 characters
- Use descriptive variable names

### Function Documentation
All functions must have docstrings:
```python
def example_function(param1: str, param2: int = 0) -> bool:
    """
    Brief description of the function.

    Parameters:
    param1 (str): Description of parameter.
    param2 (int): Description with default value.

    Returns:
    bool: Description of return value.

    Raises:
    ValueError: When parameter is invalid.
    """
    # Implementation here
    pass
```

### Error Handling
- Use try-except blocks for external dependencies
- Provide meaningful error messages in English
- Log errors appropriately for debugging

### Constants
Define constants at module level:
```python
# Good
DEFAULT_CAMERA_INDEX = 0
IMAGE_SIZE = (224, 224)

# Avoid magic numbers in code
```

## Testing Guidelines

### Test Structure
```python
def test_function_name():
    """Test description."""
    # Arrange
    input_data = "test_input"
    
    # Act
    result = function_to_test(input_data)
    
    # Assert
    assert result == expected_output
```

### Test Categories
1. **Unit Tests**: Test individual functions
2. **Integration Tests**: Test module interactions
3. **Mind+ Tests**: Test block functionality in Mind+ environment

### Running Tests
```bash
# Run all tests
python -m pytest

# Run specific test file
python -m pytest test/test_learn.py

# Run with coverage
python -m pytest --cov=python/libraries
```

## Documentation

### README Updates
When adding features, update:
- Block descriptions
- Usage examples
- Dependency requirements
- Version information

### Code Comments
- Explain complex algorithms
- Document workarounds and platform-specific code
- Use English for all comments

### Examples
Provide working examples for new features:
```python
# Example: Using new feature
model = load_custom_model("model.keras")
result = new_feature(model, additional_params)
print(f"Result: {result}")
```

## Issue Reporting

### Bug Reports
Include:
- Mind+ version
- Python version
- Operating system
- Steps to reproduce
- Expected vs actual behavior
- Error messages/screenshots

### Feature Requests
Include:
- Educational use case
- Proposed implementation approach
- Compatibility considerations
- Examples of similar features

## Educational Focus

Remember this is an educational project:
- **Clarity over complexity**: Choose readable code over clever tricks
- **Documentation**: Explain why, not just what
- **Examples**: Provide practical, working examples
- **Accessibility**: Consider different skill levels

## Review Process

All contributions go through:
1. **Automated checks**: Code style, tests
2. **Peer review**: Code quality, documentation
3. **Educational review**: Learning value, clarity
4. **Testing**: Mind+ compatibility verification

## Recognition

Contributors will be:
- Listed in project contributors
- Credited in relevant documentation
- Acknowledged in academic publications (with permission)

## Questions?

- **GitHub Issues**: For bugs and feature requests
- **Discussions**: For questions and ideas
- **Email**: stefano.zingaro@unibo.it for academic collaboration

Thank you for helping make computer vision education more accessible! 🚀