# --- NCP 임대 종료 시 해당 파일(pull.sh) 삭제 예정 ---
#!/bin/bash

GIT=$(which git)
${GIT} pull origin main
