# Security Policy

## Supported Versions

We provide security updates for the following versions:

| Version | Supported          |
| ------- | ------------------ |
| 2.1.x   | :white_check_mark: |
| 2.0.x   | :white_check_mark: |
| < 2.0   | :x:                |

## Reporting a Vulnerability

The MAST Computer Vision Module is an educational tool, but we take security seriously to protect students and educators.

### How to Report

1. **Email**: Send details to stefano.zingaro@unibo.it
2. **Subject**: Include "SECURITY" in the subject line
3. **Details**: Provide as much information as possible:
   - Description of the vulnerability
   - Steps to reproduce
   - Potential impact
   - Affected versions
   - Any proposed solutions

### What to Expect

- **Acknowledgment**: We'll respond within 48 hours
- **Assessment**: Initial assessment within 1 week
- **Updates**: Regular updates on investigation progress
- **Resolution**: Fix timeline based on severity

### Security Considerations

This module handles:
- **Webcam Access**: Local camera permissions
- **File Operations**: Local file system access
- **Network Requests**: API communications for data transmission
- **Model Loading**: Local and remote model files

### Safe Usage Guidelines

1. **Network Security**:
   - Only use trusted API endpoints
   - Validate SSL certificates for HTTPS connections
   - Be cautious with model downloads from unknown sources

2. **File System Security**:
   - Models are stored in user's home directory
   - Webcam images are saved locally with timestamps
   - No automatic file cleanup (users control retention)

3. **Privacy Considerations**:
   - Webcam images contain potentially sensitive data
   - API transmissions include base64-encoded images
   - Consider data privacy laws in your jurisdiction

4. **Educational Environment**:
   - Designed for supervised learning environments
   - Instructors should review API endpoints used by students
   - Consider network policies for classroom deployment

### Known Security Features

- **Input Validation**: Path and parameter validation implemented
- **Error Handling**: Graceful error handling without exposing internals
- **No Dynamic Code Execution**: No eval() or exec() usage
- **Timeout Protection**: API requests have timeout limits
- **Resource Management**: Proper webcam resource cleanup

### Responsible Disclosure

We follow responsible disclosure practices:
- Security issues are addressed promptly
- Fixes are released as soon as possible
- Public disclosure after fixes are available
- Credit given to security researchers (with permission)

### Educational Context

Remember this is an educational tool:
- Used in supervised classroom environments
- Students should be guided on security best practices
- Instructors should review and approve API integrations
- Consider local deployment for sensitive environments

Thank you for helping keep MAST educational tools secure!