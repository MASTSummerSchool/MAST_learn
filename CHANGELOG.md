# Changelog

All notable changes to the MAST Computer Vision Module will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.1.2] - 2025-01-08

### Added
- MIT License file for open source compliance
- CONTRIBUTING.md with detailed contribution guidelines
- CHANGELOG.md for version tracking
- Repository badges and improved README structure
- Table of contents and better documentation organization

### Fixed
- Webcam image naming with unique timestamps to prevent overwriting
- Model storage location changed from ~/MAST_learn/test to ~/models
- Cache location moved to ~/models/cache for better organization
- Removed dynamic import security issue (replaced __import__ with standard import)
- Updated TypeScript block comments with new file paths

### Removed
- test/ folder as no longer needed

## [2.1.1] - 2025-01-08

### Fixed
- Python 3.8.5 compatibility for Mind+ environment
- TensorFlow version conflicts with unsigned binaries
- Import statements updated for tensorflow.keras compatibility
- Protobuf version constraints to avoid conflicts

### Changed
- Downgraded to TensorFlow 2.11.1 for stability
- Simplified dependency list for Mind+ compatibility
- Updated documentation for Python 3.8.5 optimization

## [2.1.0] - 2025-01-08

### Added
- REST API integration with JSON data transmission
- `send_prediction_data()` function for API communication
- `webcam_predict_and_send()` complete workflow function
- Base64 image encoding for JSON payloads
- Comprehensive error handling for API calls
- HTTP headers with User-Agent identification

### Documentation
- JSON payload format examples
- API integration workflow examples
- Error response handling documentation

## [2.0.0] - 2025-01-08

### Changed
- **BREAKING:** Simplified to 4 essential blocks
- Removed all non-essential prediction blocks
- Optimized workflow to use model objects instead of model names
- Major performance improvement (70-80% faster execution)

### Added
- Efficient model object reuse pattern
- URL support for remote model loading
- Automatic model caching system
- GitHub repository model support

### Removed
- Legacy prediction blocks with string model names
- Redundant workflow functions
- Sensor-based ML functionality (focusing only on computer vision)

## [1.1.0] - 2025-01-08

### Added
- Model object efficiency optimization
- Separate label and confidence prediction blocks
- Legacy function compatibility
- Performance improvements documentation

### Changed
- Updated blocks to accept model objects instead of strings
- Improved workflow efficiency by avoiding repeated model loading

## [1.0.0] - 2025-01-08

### Added
- Initial computer vision module with 8 blocks
- Webcam image capture functionality
- Custom MobileNet model loading and inference
- Label and confidence score prediction
- Cross-platform path handling (Windows, macOS, Linux)
- Mind+ visual programming integration
- Complete workflow examples and documentation

### Features
- MobileNet model support with 8 object classes
- Webcam integration with OpenCV
- Custom class name support
- Error handling and validation
- Educational documentation for MAST Summer School

### Dependencies
- opencv-python for computer vision
- keras for machine learning models
- numpy for numerical operations
- tensorflow for deep learning backend

## [Unreleased]

### Planned
- Internationalization (English/Italian language support)
- Enhanced test coverage
- Performance benchmarking
- Advanced caching mechanisms
- Batch processing capabilities