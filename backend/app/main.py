<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Thai Consonant Drill</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    
    <style>
        body {
            margin: 0;
            font-family: Arial, sans-serif;
            background-color: #f1f3f4;
            text-align: center;
        }

        header {
            background-color: #ffffff;
            padding: 20px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }

        header h1 {
            margin: 0;
            font-size: 28px;
            color: #202124;
        }

        .container {
            max-width: 500px;
            margin: 40px auto;
            background-color: white;
            border-radius: 12px;
            padding: 30px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }

        input {
            padding: 10px 12px;
            width: 80%;
            border-radius: 8px;
            border: 1px solid #ccc;
            font-size: 16px;
            margin-bottom: 15px;
        }

        button {
            padding: 12px 24px;
            background-color: #1a73e8;
            color: white;
            border: none;
            border-radius: 8px;
            font-size: 16px;
            cursor: pointer;
        }

        button:hover {
            background-color: #1557b0;
        }

        #quizSection {
            display: none;
            margin-top: 30px;
        }

        #nicknameDisplay {
            font-size: 20px;
            font-weight: bold;
            margin-bottom: 15px;
            color: #202124;
        }

        #question {
            font-size: 72px;
            margin: 25px 0;
        }

        .choice {
            display: block;
            width: 100%;
            margin: 10px 0;
            padding: 12px;
            background-color: #e8eaed;
            border: none;
            border-radius: 8px;
            font-size: 16px;
            cursor: pointer;
        }

        .choice:hover {
            background-color: #d2d5d8;
        }

        footer {
            text-align: center;
            padding: 15px;
            font-size: 14px;
            color: #666;
        }
    </style>
</head>

<body>

<header>
    <h1>CSII Team X presents</h1>
    <p>Thai Consonant Drill</p>
</header>

<div class="container">
    <div id="startSection">
        <input type="text" id="nickname" placeholder="Enter your nickname">
        <br>
        <button onclick="startQuiz()">Start Quiz</button>
    </div>

    <div id="quizSection">
        <div id="nicknameDisplay"></div>
        <p>Remaining: 36</p>
        <h2>Thai Consonant Drill</h2>
        <div id="question">พ</div>

        <button class="choice">phor phan — Low</button>
        <button class="choice">hor hip — High</button>
        <button class="choice">tor tao — Middle</button>
    </div>
</div>

<footer>
    © 2026 Thai Consonant Drill
</footer>

<script>
    function startQuiz() {
        const nickname = document.getElementById("nickname").value.trim();

        if (nickname === "") {
            alert("Please enter your nickname.");
            return;
        }

        document.getElementById("nicknameDisplay").innerText = nickname;
        document.getElementById("quizSection").style.display = "block";
    }
</script>

</body>
</html>
