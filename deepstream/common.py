CODEC_MP4 = "MP4"
CODEC_H265 = "H265"
CODEC_H264 = "H264"
USBCAM_PROTOCOL = "v4l2://"  # Invented by us since there's no URI for this
RASPICAM_PROTOCOL = "argus://"  # Invented by us since there's no URI for this
CONFIG_FILE = "config_maskcam.txt"  # Also used in nvinfer element

# Available commands (to send internally, between processes or via MQTT)
CMD_FILE_SAVE = "save_file"
CMD_STREAMING_START = "streaming_start"
CMD_STREAMING_STOP = "streaming_stop"
CMD_INFERENCE_RESTART = "inference_restart"
