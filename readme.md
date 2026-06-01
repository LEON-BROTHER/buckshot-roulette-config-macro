# Buckshot Roulette Config for Lobbys via pyautogui 
> Note: I did this in like 1-2 hours. If you find any issues send a issue or a pull request to fix the issue. 
> And yea, I did use 3 monitors but I was lazy to add it in for a personal project. 


## How to install

You need python for this script

1. Download the script

2. Install pyautogui 

<code>pip install pyautogui</code>

If that doesn't work, use requirements.txt

3. Run and boom it works. (Hopefully)

Run this script only in the match options screen!!

## Config editing

> Note: The Python script does not validate any values to 100%.

### Global Config
<table>
	<thead>
		<tr>
            <th>Field</th>
            <th>Values</th>
        </tr>
	</thead>
	<tbody>
		<tr>
            <td>number_of_rounds</td>
            <td>1 - 3</td>
        </tr>
        <tr>
            <td>skip_intro</td>
            <td>true / false</td>
        </tr>
	</tbody>
</table>
<br>

### Round config

> Note: -1 => Random
<table>
	<thead>
		<tr>
            <th>Field</th>
            <th>Values</th>
        </tr>
	</thead>
	<tbody>
		<tr>
            <td>starting_health</td>
            <td>Range: 1 - 6 or -1</td>
        </tr>
        <tr>
            <td>items</td>
            <td>list of items</td>
        </tr>
        <tr>
            <td>sequences</td>
            <td>list of sequences</td>
        </tr>
	</tbody>
</table>
<br>


#### Item config
<table>
	<thead>
		<tr>
            <th>Field</th>
            <th>Values</th>
        </tr>
	</thead>
	<tbody>
		<tr>
            <td>name of the item</td>
            <td>just don't touch it</td>
        </tr>
        <tr>
            <td>max per player</td>
            <td>1 - 8</td>
        </tr>
        <tr>
            <td>max on table</td>
            <td>1 - 32</td>
        </tr>
        <tr>
            <td>is enabled</td>
            <td>true / false</td>
        </tr>
	</tbody>
</table>
<br>

#### Sequence config
> Note: -1 => Random

> The sum of lives and blanks can only be a max of 10
<table>
	<thead>
		<tr>
            <th>Field</th>
            <th>Values</th>
        </tr>
	</thead>
	<tbody>
		<tr>
            <td>number of blanks</td>
            <td>-1 - 10</td>
        </tr>
        <tr>
            <td>number of lives</td>
            <td>-1 - 10</td>
        </tr>
        <tr>
            <td>number of items</td>
            <td>-1 - 8</td>
        </tr>
	</tbody>
</table>
<br>
