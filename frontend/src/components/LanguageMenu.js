import * as React from 'react';
import Button from '@mui/material/Button';
import Menu from '@mui/material/Menu';
import MenuItem from '@mui/material/MenuItem';
import { Radio, RadioGroup, FormControl, FormLabel, FormControlLabel } from '@mui/material';
import { useTranslation } from 'react-i18next';

function LanguageMenu() {
    const { t, i18n } = useTranslation();
    const [anchorEl, setAnchorEl] = React.useState(null);
    const open = Boolean(anchorEl);
    const handleClick = (event) => {
        setAnchorEl(event.currentTarget);
    };
    const handleClose = () => {
        setAnchorEl(null);
    };

    const changeLanguage = (lng) => {
        i18n.changeLanguage(lng);
        handleClose();
    };
    return (
        <div>
            <Button color="inherit" onClick={handleClick}>{t("language.label")}</Button>
            <Menu
                id="basic-menu"
                anchorEl={anchorEl}
                open={open}
                onClose={handleClose}
                MenuListProps={{
                    'aria-labelledby': 'basic-button',
                }}>
                <MenuItem onClick={() => changeLanguage("en")}>{t("language.en")}</MenuItem>
                <MenuItem onClick={() => changeLanguage("mr")}>{t("language.mr")}</MenuItem>
            </Menu>
        </div>
    );
}

export default LanguageMenu;