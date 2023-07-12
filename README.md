# Rename Move.AI Session Files

This Python script renames files received from a Move.AI recording session to be used in the Move.AI web interface. 

The original file names will be in a format similar to this:
```
CB52F206-79E6-4AD8-9F35-5D82C36D3BF9_386C8431-4E56-429D-A5FD-83F17662BDEA_FCC4E042-525C-48CC-A168-D4095B07F739.mov
```

The script renames these to follow the naming standard of first the camera ID and then the take name, e.g., 
`cam01_Take01.mov`

*Please note: This tool is designed for Move.AI version 1.11.0 as of July 2023.*

## Requirements

- Python 3.7 or above

## Installation

Clone this repository to your local machine:

```bash
git clone https://github.com/LinusHe/moveai-renamer.git
```
and navigate in the folder:
```bash
cd moveai-renamer
```


## Usage

Make sure you have your `.mov` files along with a `session.json` in the same directory.

Run the script from the command line like this:

```bash
python rename.py <directory> <session.json>
```


Where:
- `<directory>` is the directory that contains the `.mov` files to be renamed.
- `<session.json>` is the json file that contains the settings for your Move.AI session.

Example:

```bash
python rename.py . session.json
```


## How it Works

The script reads the session's settings from the provided json file and extracts relevant information such as device information and scene takes. Then, it iterates through each `.mov` file in the specified directory, renames it according to the cameraID and take name, and ensures that no two files end up with the same name.

## Troubleshooting

If you encounter any issues with the script, please open an issue on this GitHub repository.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

