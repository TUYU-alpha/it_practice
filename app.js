const quiz = [
  {
    question:'ゲーム市場、最も売れたゲーム機は次のうちどれ？',
    answers:[
      'スーパーファミコン',
      'プレイステーション2',
      'ニンテンドースイッチ',
      'ニンテンドーDS'
    ],
    correct:'ニンテンドーDS'
  }, {
    question:'ねこのかわいいところはどれ？',
    answers:[
      '鳴き声',
      'しぐさ',
      '愛嬌',
      '寝顔'
    ],
    correct:'愛嬌'
  }, {
    question:'大損害を受けた時の金額はどれ？',
    answers:[
      '4万',
      '5万',
      '7万',
      '11万'
    ],
    correct:'5万'
  }
];
const quizLength =quiz.length;
let quizIndex = 0;
let score = 0;

const $button = document.getElementsByName('Primary');
const $reloadButton = document.getElementById('js-reload');
const buttonLength = $button.length;
//クイズの問題文、選択肢を定義
const setupQuiz = () => {
  document.getElementById('js-question').textContent = quiz[quizIndex].question ;
  let buttonIndex = 0;
  while(buttonIndex < buttonLength){
    $button[buttonIndex].textContent = quiz[quizIndex].answers[buttonIndex];
    buttonIndex ++;
  }
}
setupQuiz();

const clickHandler = (e) => {
  if(quiz[quizIndex].correct === e.target.textContent){
   window.alert('正解！');
   score ++;
 } else {
   window.alert('不正解！');
 }

 quizIndex++;

 if(quizIndex < quizLength){
   //問題数があれば実行
   setupQuiz();
 }else{
   //もんでい数がなければ終了
   window.alert('終了！あなたの正解数は'+ score + '/' + quizLength + 'です！');
 }
}


let handlerIndex = 0;
while(handlerIndex < buttonLength){
  $button[handlerIndex].addEventListener('click', (e) =>{
    clickHandler(e);
  });
  handlerIndex ++;
}

$reloadButton.textContent = "もう一度挑戦する";

$reloadButton.addEventListener('click', )
