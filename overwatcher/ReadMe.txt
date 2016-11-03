Dependencies:

# can probably pip install these
scipy
numpy-1.11 or so (numpy+mkl on Windows)
ffmpeg

# might need a binary on windows
opencv-3.1.0

# mac opencv3 instructions:
brew tap homebrew/science
brew install -d homebrew/science/opencv3 --with-examples --with-contrib --HEAD

# get pygame from brew, or binary on windows
brew install homebrew/python/pygame

# ... then install the stuff from the requirements file.
pip install -r requirements.txt
