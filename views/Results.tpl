<table>
<tr><td>
<b>(1) FIND COUNT & PERCENTAGE OF EMPLOYEES WHO FAILED IN TERM-1, PASSING SCORE = 37 ::<br> <b>------------------------------------------------------------------------------------------------------------------------------------------------<br>
</td></tr>
%for list in Output1:
    <tr>
        <td>{{list}} </td>
    </tr>
%end
</table>
<br>


<table>
<tr><td>
<b>(2) FIND EMPLOYEES WHO FAILED IN AGGREGATE (TERM-1 + TERM-2 + TERM-3) ::<br> <b>--------------------------------------------------------------------------------------------------------------------------<br>
</td></tr>
%for list in Output2:
    <tr>
        <td>{{list}} </td>
    </tr>
%end
</table>

<br>
<table>
<tr><td>
<b>(3) FIND THE AVERAGE SCORE OF TRAINEES FOR TERM-1 ::<br> <b>-----------------------------------------------------------------------------------------<br>
</td></tr>
%for list in Output3:
    <tr>
        <td>{{list}} </td>
    </tr>
%end
</table>


<br>
<table>
<tr><td>
<b>(4) FIND THE AVERAGE SCORE OF TRAINEES FOR AGGREGATE (TERM-1 + TERM-2 + TERM-3)   ::<br> <b>--------------------------------------------------------------------------------------------------------------------------------------------<br>
</td></tr>
%for list in Output4:
    <tr>
        <td>{{list}} </td>
    </tr>
%end
</table>


<br>
<table>
<tr><td>
<b>(5) FIND THE AVERAGE SCORE OF TRAINEES FOR AGGREGATE (TERM-1 + TERM-2 + TERM-3)   ::<br> <b>--------------------------------------------------------------------------------------------------------------------------------------------<br>
</td></tr>
    <tr>
        <td>>>>>>>> TOTAL COUNT :: {{Output5}} </td>
    </tr>
</table>


<br>
<table>
<tr><td>
<b>(6) FIND THE NUMBER OF EMPLOYEES WHO FAILED IN ANY OF THE 3 TERMS(TERM-1 + TERM-2 + TERM-3)   ::<br> <b>-----------------------------------------------------------------------------------------------------------------------------------------------------------------<br>
</td></tr>
    <tr>
        <td>>>>>>>> TOTAL COUNT :: {{Output6}} </td>
    </tr>
</table>