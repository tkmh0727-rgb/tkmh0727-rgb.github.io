# Myeonghyeon Kim · Academic CV

GitHub Pages: https://tkmh0727-rgb.github.io/

## CV 수정

1. `data/cv.json`에서 학력, 경력, 논문, 프로젝트, 수상, 교육 내용을 수정합니다.
2. Python 3로 `python build.py`를 실행합니다. 외부 패키지는 필요하지 않습니다.
3. 생성된 HTML 5개와 데이터 변경을 함께 커밋합니다.
4. 로컬 확인: `python -m http.server 8000` 실행 후 `http://localhost:8000`을 엽니다.
5. 기본 브랜치에 반영되면 기존 GitHub Pages 설정에 따라 게시됩니다.

HTML은 정적으로 생성되어 JavaScript 없이 읽을 수 있습니다. 기존 페이지 주소를 유지합니다. 전체 CV는 메인 페이지에서 브라우저 인쇄(Ctrl+P / Cmd+P)로 PDF 저장할 수 있습니다.

## 기록 기준

- 논문 제목, 저자 순서, 학회명은 최종 원고를 기준으로 입력합니다.
- `kind`: `journal`, `conference`, `manuscript`. `status`는 실제 확인된 상태를 입력합니다.
- 채택, 발표 완료, 게재는 서로 다른 상태입니다. 초안이나 참가 등록만으로 발표·게재 완료를 표시하지 않습니다.
- 같은 연구를 서로 다른 행사에서 발표했다면 행사별 항목을 구분합니다. 단순 원고 버전은 별도 실적으로 세지 않습니다.
- 지원서 작성이나 탈락·중단된 지원은 수상·연구비 수혜·현재 연구로 추가하지 않습니다.
- 개인 증빙 원본, 서명, 학번, 주소, 재정정보, 내부 보고서는 저장소에 올리지 않습니다. 공개할 CV 문구만 기록합니다.
- `updated`를 실제 수정일로 갱신합니다. 날짜가 지났다는 이유만으로 연구 상태를 자동 변경하지 않습니다.

## 페이지

- `index.html`: 전체 CV
- `research.html`: 연구 방향과 석사 연구
- `projects.html`: 구현·실험 경험
- `publications.html`: 논문·학회 기여·원고
- `achievements.html`: 수상·장학금·교육

공개 데이터는 `data/cv.json`, 공통 렌더링은 `build.py`, 스타일은 `theme.css`에서 수정합니다.
