# VS Code 확장 기능에 오신 것을 환영합니다

## 폴더 내용

* 이 폴더에는 확장 기능에 필요한 모든 파일이 포함되어 있습니다.
* `package.json` - 이 파일은 확장 기능과 명령을 선언하는 매니페스트 파일입니다.
  * 샘플 플러그인은 명령을 등록하고 그 제목과 명령 이름을 정의합니다. 이 정보를 통해 VS Code는 명령 팔레트에 명령을 표시할 수 있습니다. 플러그인을 아직 로드할 필요는 없습니다.
* `src/extension.ts` - 이 파일은 명령의 구현을 제공하는 메인 파일입니다.
  * 이 파일은 `activate`라는 하나의 함수를 내보내며, 이는 확장 기능이 처음 활성화될 때 호출됩니다 (이 경우 명령을 실행하여 활성화). `activate` 함수 내부에서 `registerCommand`를 호출합니다.
  * 명령의 구현을 포함하는 함수를 `registerCommand`의 두 번째 매개변수로 전달합니다.

## 설정

* 추천 확장 기능을 설치하세요 (amodio.tsl-problem-matcher, ms-vscode.extension-test-runner, dbaeumer.vscode-eslint).

## 바로 시작하기

* `F5` 키를 눌러 확장 기능이 로드된 새 창을 엽니다.
* 명령 팔레트에서 (`Ctrl+Shift+P` 또는 Mac에서는 `Cmd+Shift+P`) `Hello World`를 입력하여 명령을 실행합니다.
* `src/extension.ts` 내부에 중단점을 설정하여 확장 기능을 디버그합니다.
* 디버그 콘솔에서 확장 기능의 출력을 확인합니다.

## 변경 사항 적용

* `src/extension.ts`의 코드를 변경한 후 디버그 툴바에서 확장을 다시 시작할 수 있습니다.
* 또한, VS Code 창을 다시 로드 (`Ctrl+R` 또는 Mac에서는 `Cmd+R`)하여 변경 사항을 로드할 수 있습니다.

## API 탐색

* `node_modules/@types/vscode/index.d.ts` 파일을 열면 전체 API 세트를 확인할 수 있습니다.

## 테스트 실행

* [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner)를 설치하세요.
* **Tasks: Run Task** 명령을 통해 "watch" 작업을 실행하세요. 이 작업이 실행 중인지 확인하지 않으면 테스트를 발견하지 못할 수 있습니다.
* 활동 막대에서 테스트 뷰를 열고 "Run Test" 버튼을 클릭하거나 단축키 `Ctrl/Cmd + ; A`를 사용하세요.
* 테스트 결과 뷰에서 테스트 결과 출력을 확인하세요.
* `src/test/extension.test.ts`를 변경하거나 `test` 폴더 내에 새로운 테스트 파일을 생성하세요.
  * 제공된 테스트 러너는 `**.test.ts` 이름 패턴과 일치하는 파일만 고려합니다.
  * 원하는 방식으로 테스트를 구조화하기 위해 `test` 폴더 내에 폴더를 생성할 수 있습니다.

## 더 나아가기

* [확장 기능 번들링](https://code.visualstudio.com/api/working-with-extensions/bundling-extension)을 통해 확장 기능의 크기를 줄이고 시작 시간을 개선하세요.
* VS Code 확장 기능 마켓플레이스에 [확장 기능을 게시](https://code.visualstudio.com/api/working-with-extensions/publishing-extension)하세요.
* [지속적 통합](https://code.visualstudio.com/api/working-with-extensions/continuous-integration)을 설정하여 빌드를 자동화하세요.

